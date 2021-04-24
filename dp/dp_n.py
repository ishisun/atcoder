import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    dp = [500*10**9]*N
    dp[N-1] = 0
    for i in range(N-1, 0, -1):
        for k in range(0,i-1):
            c = [0] * i
            c[k] = a[k] + a[k+1]
        k = c.index(min(c))
        dp[i-1] = min(dp[i-1],dp[i] + c[k])
        if k == 0:
            a = c[k:k] + a[k+1:-1]
        elif k == i-2:
            a = a[0:k-1] + c[k:k]
        else:
            a = a[0:k-1] + c[k:k] +a[k+2:-1]
    print(dp[1])



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
