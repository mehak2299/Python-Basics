s=input("Enter String")
length=len(s)
half=length//2
first=s[:half:]
second=s[half:length:1]
if first==second:
    print("String is Symmetrical")
print(s)
print("Length",length,"half",half)
print("first : ",first)
print('Second',second)


# string = 'amaama'
# length = len(string)
# half = length // 2

# first_str = string[:half]
# second_str = string[half + length % 2:]
#
# # symmetric
# if first_str == second_str:
#     print(string, 'string is symmetrical')
# else:
#     print(string, 'string is not symmetrical')
#
# # palindrome
# if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
#     print(string, 'string is palindrome')
# else:
#     print(string, 'string is not palindrome')
