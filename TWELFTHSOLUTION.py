h,s1,s2 = map(int,input().split())

if h>50 and s1>60 and s2>100:
    print("10")
elif(h>50 and s1>60):
    print("9")
elif(s1>60 and s2>100):
    print("8")
elif(h>50 and s2>100):
    print("7")
elif(h>50 and s1>60 or s2>100):
    print("6")
else:
    print("5")
