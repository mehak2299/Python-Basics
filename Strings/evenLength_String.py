s=input("Enter String")
n=s.split()
string=[i for i in n if len(i)%2==0]
print("STRIMG",''.join(string))