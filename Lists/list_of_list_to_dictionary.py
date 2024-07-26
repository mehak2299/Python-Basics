test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
res={}
for i in test_list:
    res[tuple(i[:2])]=tuple(i[2:])
print(res)

res1={tuple(i[:2]):tuple(i[2:])for i in test_list}
print(res1)