import sys
from io import StringIO
import unittest
import bisect

def resolve():
    N, K = map(int,input().split())
    a = list(map(int,list(input().split())))
    b = list(map(int,list(input().split())))
    a.sort()
    b.sort()
    C = a[-1] * b[-1]
    c = range(1,C+1)
    left = 0
    right = C
    while left < right - 1:
        center = (left + right)//2
        count = 0
        for i in range(N):
            count += bisect.bisect_right(b, center//a[i])
        if  K <= count:
            right = center
        else:
            left = center
    print(right)



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
        input = """2 3
2 3
3 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 7
1 2 1
2 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 8
701687787 500872619 516391519 599949380
458299111 633119409 377269575 717229869"""
        output = """317112176525562171"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
