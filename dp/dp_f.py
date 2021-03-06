import sys
from io import StringIO
import unittest

def resolve():
    s = input()
    t = input()

    dp =[[0]*(len(t)+1) for _ in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i][j] + 1,dp[i][j])
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j+1])
    ans_len = dp[-1][-1]
    i = len(s)
    j = len(t)
    ans = ""

    while (i>0 and j>0):
        if dp[i][j] == dp[i][j-1]:
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            ans = s[i-1] + ans
            i -= 1
            j -= 1
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
        input = """axyb
abyxb"""
        output = """axb"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aa
xayaz"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a
z"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """abracadabra
avadakedavra"""
        output = """aaadara"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
