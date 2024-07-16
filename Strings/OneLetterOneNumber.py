import re


def check(str):
    flag_n=False
    flag_c=False
    for i in str:
        if i.isalpha():
            flag_c=True
        if i.isdigit():
            flag_n=True
    return  flag_c,flag_n

def check1(str):
    match=re.search(r'[a-zA-Z]+',str)and re.search(r'[0-9]+',str)
    if match:
        return True
    else:
        return False
print(check("agc112"))
print(check(("agc")),"d")