str='Mango Icecream'
freq=''
for char in str.lower():
    if char in freq:
        pass
    else:
        freq+=char

print(freq)

# Without Order

s=set(str.lower())
s=''.join(s)
print(s)