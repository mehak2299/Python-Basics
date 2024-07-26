list1 = [11, 5, 17, 18, 23, 50]
list2 = [11, 5, 17, 18, 23, 50]
list3 = [11, 5, 17, 18, 23, 50]

for i in list1:
    if i%2==0:
        list1.remove(i)
print(list1)
list2=[i for i in list2 if i%2!=0]
print(list2)

del list3[1:5]
print(list3)