n=int(input())
x=n%8
if(x==0):
    x=8
if(x==7):
    print("%dSU"%(n+1))
if(x==8):
    print("%dSL"%(n-1))
if(x==1):
    print("%dLB"%(n+3))
if(x==4):
    print("%dLB"%(n-3))
if(x==2):
    print("%dMB"%(n+3))
if(x==5):
    print("%dMB"%(n-3))
if(x==3):
    print("%dUB"%(n+3))
if(x==6):
    print("%dUB"%(n-3))    
