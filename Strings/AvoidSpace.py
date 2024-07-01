s=input("Enter String")
m=[i for i in s if i !=' ']
print("VALUE : ",len(m),m)

res=(not chr.isspace() for chr in s)
print(sum(res))

str1=s.replace(' ','')
res1=len(str1)
print(len(str1))

# List comphrehension
res2=len(''.join([char for char in s if char!=' ']))
print("RES2",res2)