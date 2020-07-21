lst = [5, 4, 1, 2, 3, 8, 7, 9]
fl = 0
sl = 0
for i in lst:
    if i > fl:
        fl = i
print(fl)
for i in lst:
    if i > sl and i != fl:
        sl = i
print(sl)
