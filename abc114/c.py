import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    print(sitigo("0",N))


def sitigo(s,N):
    if int(s) > N:
        return 0
    count = 1 if all(s.count(c) > 0 for c in "753") else 0
    for c in "753":
        count += sitigo(s + c, N)
    return count


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
        input = """575"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3600"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999999"""
        output = """26484"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
