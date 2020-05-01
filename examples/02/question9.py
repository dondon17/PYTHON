a = dict()
print("a = {}".format(a))
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' - dictionary의 key값으로 list는 불가능!!
a[250] = 'python'
print("a = {}".format(a))