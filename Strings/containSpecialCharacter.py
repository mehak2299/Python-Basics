import re
string="sabsf"
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
print((regex.search(string)==None))
if (regex  .search(string)==None):
    print("String is accepted")
else:
    print("String is not accepted")