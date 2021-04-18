N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans =[]

for ai in A:
    if not ai in B:
        ans.append(ai)

for bi in B:
    if not bi in A:
        ans.append(bi)

ans.sort()

ans = " ".join(map(str,ans))
print(ans)
