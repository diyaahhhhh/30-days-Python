#Task 1

number=int(input("Enter a number: "))
if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is 0")

#Task 2

age=int(input("Enter age: "))
if 0<=age<=12:
    print("Child")
elif 13<=age<=19:
    print("Teenager")
else:
    print("Adult")