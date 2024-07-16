import re
str='abscdei'
vowels='aeiouAEIOU'

ans=sum(str.count(i) for i in vowels)
print(ans)

one=0
for i in str:
    if i in vowels:
        one+=1

print("No of Vowels",one)

two=[i for i in str if i in vowels]
print(len(two))

# Using Regex

str1='abscdei'
vowels1=r'[aeiouAEIOU]'
count1=len(re.findall(vowels1,str1))
print(count1)
