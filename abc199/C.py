import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    S = list(input())
    Q = int(input())
    tab = [list(map(int, input().split())) for _ in range(Q)]
    T, A, B = [list(i) for i in zip(*tab)]
    count = 0
    for i in range(Q):
        if T[i] == 1:
            S[(A[i]-1+count)%(2*N)], S[(B[i]-1+count)%(2*N)] = S[(B[i]-1+count)%(2*N)], S[(A[i]-1+count)%(2*N)]
        else:
            count += N
    if count % (2*N) ==0:
        ans = "".join(S)
    else:
        ans = "".join(S[N:2*N])+"".join(S[0:N])
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
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
