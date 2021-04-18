import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    A = list(set(list(map(int, input().split()))))
    A.sort()
    ans = A[0] + 1
    for i in range(1, len(A)):
        ans = ans * ( A[i] + 1 -A[i-1])
    ans = ans % (10**9 +7)
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
        input = """2
1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 3 4 1 5 2"""
        output = """32"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
314 159 265 358 979 323 846"""
        output = """492018656"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
