def check(str):

    vowels = 'aeiou'
    s=[v for v in vowels if v in str]
    if len(s)==len(vowels):
        print("Acceopted")
    else:
        print("Not Accepted")
def check1(str):
    vowels = {'a','e','i','o','u'}
    s=set(str.lower())
    print(s)
    if vowels<s:
        print("Accepted")
    else:
        print("Not Accepted")

if __name__=="__main__":
    str = 'aeikds'
    check(str)
    check1(str)