# Tuples are immutable
# Elements can not change
# However, elements of nested elements can be changed.

my_tuple = (3, 5, ['a', 'b', 'c'], 56)
print(my_tuple) # original tuple

my_tuple[2][1] = 'x'
print(my_tuple) # tuple after changing element


# Tuples can also be re-assigned

my_tuple1 = (1, 2, 3)
print(my_tuple1)

my_tuple1 = ('a', 'b', 'c')
print(my_tuple1)