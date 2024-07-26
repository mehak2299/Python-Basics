test_list = [5, 6, [], 3, [], [], 9]
res=filter(None,test_list)
print(list(res))

test_list1 = [5, 6, [], 3, [], [], 9]
res1=[i for i in test_list1 if i!=[]]
print(res1)