x=int(input())
y=int(input())
z=int(input())
a=int(input())
p=int(input())
c=0
t=[]

for i in range(p+1):
    for j in range(p+1):
        for k in range(p+1):
            for l in range(p+1):
                if(x*i+y*j+z*k+a*l)==p:
                    print("# of PINK is %d # of GREEN is %d # of RED is %d # of ORANGE is %d"%(i,j,k,l))
                    c=c+1
                   
                    t.append(i+j+k+l)
                    
                    
                    
print("Total combinations is",c)
print("Minimum number of tickets to print is",min(t))
