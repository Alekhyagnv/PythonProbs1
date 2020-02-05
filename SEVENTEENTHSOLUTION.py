A,B,N=map(int,input().split())
while(N):
    A=A*2
    N=N-1
    if(N!=0):
        B=B*2
        N=N-1
print(A+B)
