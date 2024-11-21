shopping_list=[]
while True:
    item=input('Enter your item:')
    shopping_list.append(item)
    choice=input('Type done if finished:')
    if choice=='done':
        break
print(shopping_list)
