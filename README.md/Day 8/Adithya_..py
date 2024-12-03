num1=int(input("Enter your number_1:"))
num2=int(input("Enter your number_2:"))
num3=int(input("Enter your number_3:"))
if num1>num2 and num1>num3:
    print("The largest number is:",num1)
elif num2>num3 and num2>num1:
    print("The largest number is:",num2)
else:
    print("The largest number is:",num3)
