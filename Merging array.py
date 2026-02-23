n,m = map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
idx_a=0
idx_b=0
res=[]
while idx_a < n and idx_b < m:
    if arr1[idx_a] <= arr2[idx_b]:
        res.append(arr1[idx_a])
        idx_a += 1
    elif arr1[idx_a] > arr2[idx_b]:
        res.append(arr2[idx_b])
        idx_b += 1
res.extend(arr1[idx_a:])
res.extend(arr2[idx_b:])
print(*res)
