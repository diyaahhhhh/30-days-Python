shopping_list=[]
while True:
    item=input("enter your item:")
    shopping_list.append(item)
    choice=input("type done if finished:")
    if choice=="done":
        break
print (shopping_list)

