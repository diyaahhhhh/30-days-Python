'''
Author:Litty jomon
Date:24-11-2024
'''
number1=int(input("Enter the first number"))
number2=int(input("Enter the second number"))
number3=int(input("enter the third number"))
if number1>=number2 and number1>number3:
    print("Largest:",number1)
elif number2>=number1 and number2>=number3:
    print("Largest:",number2)
else:
    print("Largest:",number3)