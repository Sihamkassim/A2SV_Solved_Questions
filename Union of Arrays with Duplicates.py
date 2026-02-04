def findUnion(a,b):
    b=int(input)
    a=int(input)
    result=a+b
    result=set(result)
    return len(result)
if __name__ == '__main__':
    n=int(input())
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=findUnion(a,b)
    print(ans)