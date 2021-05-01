import sys
from io import StringIO
import unittest

def resolve():
    N, D, H = map(int,input().split())
    dh = [list(map(int, input().split())) for _ in range(N)]
    d, h = [list(i) for i in zip(*dh)]
    ans = 0
    for i in range(N):
        ans =max(ans, H - D*(H-h[i])/(D-d[i])) 
    print(ans)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """1 10 10
3 5"""
        output = """2.857142857142857"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 10 10
3 2"""
        output = """0.0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 896 483
228 59
529 310
339 60
78 266
659 391"""
        output = """245.3080684596577"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
