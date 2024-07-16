n=input("Enter String")
first=n[::-1].upper()
last=n[-1:-2:-1].upper()
middle=n[1:len(n)-1:1]
print(first+middle+last)