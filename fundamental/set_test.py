# new set
set_a = {1, 2, 3, 4, 5}
set_b = set([3, 4, 5, 6, 7])
set_c = {'kavy', 'kevin', 'peter', 'eric'}
set_d = {'anna', 'jane', 'kavy', 'katelyn'}
print(set_a)
print(set_b)
print(set_c)
print(set_d)

# intersection
inter = set_a & set_b
print(inter)

# union
uni = set_c & set_d
print(uni)

# difference
diff = set_b - set_a
print(diff)

# symm
symm = set_c ^ set_d
print(symm)

# in/not in
print("kavy" in set_c)
print("kavy" not in set_b)

# add
set_c.add("leo")
print(set_c)

# remove/discard/clear
set_c.remove("kavy")
print(set_c)
set_c.discard("kavy") # remove will generate error
print(set_c)
set_c.clear()
print(set_c)

# isdisjoint/issubset/issuperset
set_e = {1, 2, 3, 4, 5, 6, 7}
print(set_e)
print(set_e.isdisjoint(set_a))
print(set_e.issubset(set_a))
print(set_e.issuperset(set_a))

# update/difference_update/

set_e.update([8])
print(set_e)
set_e.difference_update(set_b)
print(set_e)
set_e.symmetric_difference_update(set_a)
print(set_e)

# frozenset
set_f = frozenset([1, 3, 5])
print(set_f)
print(set_e & set_f)

