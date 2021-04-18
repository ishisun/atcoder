import sys
from io import StringIO
import unittest

def resolve():
    

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
        output = """2 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2
1 4
2 3"""
        output = """3 2 1 4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
