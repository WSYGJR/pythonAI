#列表操作
l = [26, 60, "A", "Hello", True]
print(type(l))

#访问列表的元素
#获取
print(l[0])
print(l[-5])
#修改
l[0] = 33
print(l[0])
print(l)
#删除
del l[0]
print(l)
#遍历
for item in l:
    print(item)
