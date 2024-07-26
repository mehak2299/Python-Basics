test_list = ["geeksforgeeks is best for geeks"]
chr_list = ['e', 'b', 'g']
d={}
for i in chr_list:
    res=test_list[0].count(i)
    d[i] = res
    print(i,"",res)

print(type(d),d)