num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
num3=float(input("Enter your third number: "))
if num1>num2 and num1>num3:
	print(num1,"is the largest number")
elif num2>num3:
	print(num2,"is the largest number")
else:
	print(num3,"is the largest number")
