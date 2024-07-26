test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

keywordList=["name","number"]
res=[]
n=len(test_list)
for i in range(0,n,2):
    res.append({keywordList[0]:test_list[i] ,keywordList[1]:test_list[i+1]})

print(res)