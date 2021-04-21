import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    p = list(map(int,input().split()))
    W = sum(p)
    dp = [[0]*(W+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(W+1):
            if dp[i-1][j]:
                dp[i][j] = 1
            elif dp[i-1][j-p[i-1]]:
                dp[i][j] = 1
    print(sum(dp[N]))





class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3
2 3 5"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
1 1 1 1 1 1 1 1 1 1"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
