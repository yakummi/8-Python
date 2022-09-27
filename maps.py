def upper(s):
    return s.upper()

mylist = list(map(upper, ['test', 'work']))
print(mylist)

list_of_ints = list(map(int, '1234567'))
print(list_of_ints)