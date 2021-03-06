import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    s = [0]*(N+1)
    dp = [[500*10**20]*(N+1) for _ in range(N+1)]
    for i in range(N):
        dp[i][i+1] = 0
        s[i+1] = s[i] + a[i]
    for dif in range(2,N+1):
        for i in range(N-dif+1):
            j =  i + dif
            for k in range(i+1,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + s[j]-s[i])
    print(dp[0][N])

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
        input = """4
10 20 30 40"""
        output = """190"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
10 10 10 10 10"""
        output = """120"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1000000000 1000000000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
7 6 8 6 1 1"""
        output = """68"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
