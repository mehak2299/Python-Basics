import re
text="Hello __World 122"
pattern=r"\w+"
matches=re.findall(pattern,text)
print(matches)
# \w+ matches one or more word characters.
# re.findall finds all occurrences of the pattern in the text and returns them in a list.