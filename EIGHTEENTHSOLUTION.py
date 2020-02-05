x=int(input())
c=0
while(x):
    r=x%10
    if(r==4):
        c=c+1
    x=x//10
print(c)
