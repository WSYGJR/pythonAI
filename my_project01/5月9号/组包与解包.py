t1 = (5, 7, 9, 11)
t2 = 5, 7, 9, 11
print(type(t1))
print(type(t2))

#解包
a,b,c,d = t1
print(a,b,c,d)
a,*b,c = t1
print(a,b,c)
*a,c = t1
print(a,c)
a,*b = t1
print(a,b)
print(type(b))