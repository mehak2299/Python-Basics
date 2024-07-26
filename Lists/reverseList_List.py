test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
# for i in test_list:
#     i.reverse()
# print(test_list)

# test_list1 = [[4, 1, 6], [7, 8], [4, 10, 8]]
# for i in test_list1:
#      i.sort(reverse=True)
# print(test_list1)

arr2=[sorted(i,reverse=True)for i in test_list]
print(arr2)