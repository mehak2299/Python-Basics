str='aabbcccd'
freq={}
for char in str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)


ans1=[i for i in freq if freq[i]%2!=0]
print(ans1)
