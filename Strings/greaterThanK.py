k = 3
str = "geek for geeks"

res=str.split(" ")
ans=[i for i in res if len(i)>k]
print(ans)