s=input("Enter String")
s1=s.split()[::-1]
print(" ".join(s1))

s2=s.split()
rev=' '.join(reversed(s2))
print("REV",rev)