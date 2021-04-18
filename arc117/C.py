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
        input = """3
BWR"""
        output = """W"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
RRBB"""
        output = """W"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
BWWRBW"""
        output = """B"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
WWBRBBWB"""
        output = """R"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """21
BWBRRBBRWBRBBBRRBWWWR"""
        output = """B"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
