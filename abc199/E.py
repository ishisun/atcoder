import sys
from io import StringIO
import unittest

def resolve():
    N, M = map(int,input().split())
    xyz = [list(map(int, input().split())) for _ in range(M)]
    X, Y, Z = [list(i) for i in zip(*xyz)]
    count = 0
    for i in range(M):
        if Y[i] <= Z[i] and Y[i] <= X[i]:
            


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
        input = """3 1
2 2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
3 3 2
4 4 3"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """18 0"""
        output = """6402373705728000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
