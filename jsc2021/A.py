import sys
from io import StringIO
import unittest



def resolve():
    X, Y, Z = map(int,input().split())

    TR = Y/X
    A = int(round(Z * TR, 0))
    if A >= TR * Z:
        if A != 0:
            A = A - 1

    print(A)


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
        input = """100 200 100"""
        output = """199"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """103 971 593"""
        output = """5590"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
