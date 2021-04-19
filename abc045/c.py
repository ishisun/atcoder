import sys
from io import StringIO
import unittest

def resolve():
    A = list(map(int,list((input()))))
    sum = 0
    for i in range(2**(len(A)-1)):
        tmp = 0
        for n in range(len(A)-1):
            tmp *= 10
            tmp += A[n]
            if 2**(n) & i:
                sum += tmp
                tmp = 0
        tmp *=10
        tmp += A[-1]
        sum += tmp
    print(sum)

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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
