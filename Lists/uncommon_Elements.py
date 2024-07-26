test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

arr=[]
for i in test_list1:
    if i not in test_list2:
        arr.append(i)

for i in test_list2:
    if i not in test_list1:
        arr.append(i)


print(arr)
x=[i for i in test_list1 if i not in test_list2]+[i for i in test_list2 if i not in test_list1]
print("List : ",x)

