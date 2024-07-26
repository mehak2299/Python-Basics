import re

test_str = "geeks4feeks is No. 1 4 geeks"

count=0
for i in test_str:
    # if i>='0'and i<='9':
    if i.isdigit():
        count+=1
print("Frequency of Numbers : ",count)

res=re.findall(r"\d",test_str)
print(len(res))