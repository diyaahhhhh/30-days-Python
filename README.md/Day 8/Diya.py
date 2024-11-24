num1=int(input('Enter a number:'))
num2=int(input('Enter another number:'))
num3=int(input('Enter another number:'))
if num1>=num2 and num1>=num3:
    print('Largest:',num1)
elif num2>=num1 and num2>=num3:
    print('Largest:',num2)
else:
    print('Largest:',num3)