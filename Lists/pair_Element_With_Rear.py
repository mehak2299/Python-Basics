test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# arr=[]
# for i in test_list:
#     for j in range(len(i)-1):
#         print (i[j],i[-1])
#         arr.append()

res=[]
for i in test_list:
    res.append([[ele,i[-1]] for ele in i[:-1]])
print(res)