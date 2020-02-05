x=int(input())
a= list(map(int, input(). split()))
sum=0
change=0
for i in range(len(a)):
    sum=sum+a[i]
rem=sum%x
k=int(sum/x)
y=rem
if rem!=0:
    for i in range(len(a)):
        while(a[i]>k and rem!=0):
            a[i]=a[i]-1
            rem=rem-1
a.sort(reverse=True)
for j in range(len(a)):
    if a[j]>k:
        change=change+(a[j]-k)
print('{} {}'.format(y,change))
