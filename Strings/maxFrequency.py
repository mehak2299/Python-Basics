test_str="OKByeKBK"
res=max(test_str,key=lambda i:test_str.count(i))
print(res)

# Using Dictionary
freq={}
for char in test_str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
print(max(freq,key=lambda i:freq[i]))
print(max(freq,key=lambda i:freq.get(i)))