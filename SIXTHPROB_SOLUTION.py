x=int(input("Enter branding expenses\n"))
y=int(input("Enter travel expenses\n"))
z=int(input("Enter food expenses\n"))
p=int(input("Enter logistics expenses\n"))
total=x+y+z+p
print("Total expenses : Rs.%2f\n"%(total))
print("Branding expenses percentage : %.2f%%"%((x/total)*100))
print("Travel expenses percentage : %.2f%%"%((y/total)*100))
print("Food expenses percentage : %.2f%%"%((z/total)*100))
print("Logistics expenses percentage : %.2f%%"%((p/total)*100))