import sys
from io import StringIO
import unittest
import math
import bisect

def resolve():
    A, B, C = map(int,input().split())
    f = [0]*(100+1)
    g = [0]*(10**6+1)
    for i in range(100 + 1):
        f[i] = A * i + B*math.sin(C*i*math.pi)
    ans = bisect.bisect_left(f,100)
    for i in range(10**6 + 1 ):
        t = ans-1+(i/10**6)
        g[i] = A * t + B*math.sin(C*t*math.pi)
    print(ans-1+(bisect.bisect_left(g,100))/(10**6))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """1 1 1"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """53 82 49"""
        output = """1.63372043395339"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
