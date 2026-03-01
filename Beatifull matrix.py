cnt=0
matrix_=[]
for i in range(5):
    row = list(map(int, input().split()))
    matrix_.append(row)
 
for i in range(5):
    for j in range(5):
        if matrix_[i][j]==1:
            cnt=abs(i-2)+abs(j-2)
print(cnt)
