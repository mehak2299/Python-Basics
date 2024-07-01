string=input("Enter String")
length=len(string)
half=length//2
second=string[:half:]+ string[half::].upper()
print(second)