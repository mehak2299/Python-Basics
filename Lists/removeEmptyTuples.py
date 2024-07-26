tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]

res=[i for i in tuples if i]
print(res)

rem=filter(None,tuples)
print(list(rem))