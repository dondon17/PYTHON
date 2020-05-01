a = b = [1, 2, 3]
print("list a = {}".format(a))
print("list b = {}".format(b))
a[1] = 4
print("list a = {}".format(a))
print("list b = {}".format(b))

print("because initailized like a=b")
print("if you want to make them different, a=b[:] or copy(b)")