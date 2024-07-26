import  random
from itertools import chain
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
seq=[0,1,2]
res=random.choice(list(chain.from_iterable(test_list)))
print(res)