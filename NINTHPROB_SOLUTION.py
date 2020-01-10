x=int(input("Enter the side in cm of a square tile\n"))
y=int(input("Enter the number of square tiles available\n"))
z=int(y**0.5)
print("Area of the largest possible square is %dsqcm"%(z*z*x*x))
