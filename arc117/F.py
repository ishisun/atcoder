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
2 5 7 4 2 1"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
8 0 6 0 9 0"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 1 5 7 0 8 4 6 4 9"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
267503 601617"""
        output = """869120"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """8
418940906 38034755 396064111 43044067 356084286 61548818 15301658 35906016 20933120 211233791 30314875 25149642 42550552 104690843 81256233 63578117"""
        output = """513119404"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
