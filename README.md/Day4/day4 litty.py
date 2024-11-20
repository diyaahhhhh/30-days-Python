'''
Author:Litty jomon
description:Age determination
'''
#TASK1
number=int(input("Enter a number"))
if number>0:
    print("Number is positive")
elif number<0:
    print("Number is negative")
else:
    print("the number is zero")
#TASK2
Age=int(input("Enter your age"))
if 0<=Age<=12:
    print("The person is a child")
elif 13<=Age<=19:
    print("The person is a teenager")
else:
    print("the person is adult ")