import sys
from io import StringIO
import unittest

def resolve():
A, B = map(int, input().split())
if A == B:
    Ea = list(range(1, A+1, 1))
    Eb = list(range(-B, 0, 1))
elif A > B:
    Ea = list(range(1, A+1, 1))
    n = A // B
    m = A % B
    Eb = []
    for num in range(1, B+1):
        if num <= m:
            Eb.append(int(-1 * num * (n+1) - (n+1) / 2 * n * B))
        else:
            Eb.append(int(-1 * num * n - n / 2 * (n-1) * B))
else:
    Eb = list(range(-B, 0, 1))
    n = B // A
    m = B % A
    Ea = []
    for num in range(1, A+1):
        if num <= m:
            Ea.append(int(num * (n+1) + (n+1) / 2 * n * A))
        else:
            Ea.append(int(num * n + n / 2 * (n-1) * A))
E = Ea + Eb
ans = " ".join(map(str,E))
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
        input = """1 1"""
        output = """1001 -1001"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 4"""
        output = """-8 -6 -9 120 -97"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 5"""
        output = """323 -320 411 206 -259 298 -177 -564 167 392 -628 151"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
