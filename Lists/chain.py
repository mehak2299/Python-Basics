from itertools import chain

test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

res=list(chain(test_list))
print(res)

# a list of odd numbers
odd = [1, 3, 5, 7, 9]

# a list of even numbers
even = [2, 4, 6, 8, 10]
res1=list(chain(odd,even))
print(res1)
