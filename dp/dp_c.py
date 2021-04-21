import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    abc = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*3 for _ in range(N+1)]

    for i in range(N):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + abc[i][k])
    print(max(dp[N]))


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
        input = """3
10 40 70
20 50 80
30 60 90"""
        output = """210"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
100 10 1"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1"""
        output = """46"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
