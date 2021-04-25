import sys
from io import StringIO
import unittest
import bisect

def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort()
    C.sort()
    count = 0
    for i in range(N):
        count += bisect.bisect_left(A,B[i]) * (N - bisect.bisect_right(C,B[i]))
    print(count)

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
        input = """2
1 5
2 4
3 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1 1
2 2 2
3 3 3"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288"""
        output = """87"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
