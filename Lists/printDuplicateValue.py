list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
res=[]
for i in list1:
    if i in res:
        pass
    else:
        value=list1.count(i)
        if value>1:
            res.append(i)
        else:
            pass
print(res)

# Single Loop
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
unique=[]
duplicate=[]
for i in lis:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)

print(duplicate)

# Using Counter
from collections import Counter
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d=Counter(l1)
new_list=[i for i in d if d[i]>1]
print(new_list)

