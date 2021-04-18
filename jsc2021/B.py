N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans =[]

if B[-1] > A[-1]:
    A1 = B
    B1 = A
    B = B1
    A = A1
i=0
j=0
while i < len(A):
    if A[i] == B[j]:
        i += 1
        if j != len(B)-1:
            j += 1
    elif A[i] < B[j]:
        ans.append(A[i])
        i += 1
    else:
        if not B[j] in ans:
            ans.append(B[j])
        if j != len(B)-1:
            j += 1
        else:
            ans.append(A[i])
            i += 1

ans = " ".join(map(str,ans))
print(ans)
