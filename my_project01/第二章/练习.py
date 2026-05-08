#a = 100，b = 200，c = 300将a, b, c分别赋值给c, a, b，并输出到控制台
a = 100
b = 200
c = 300
d = a
a = c
c = b
b = d
print("a =", a)
print("b =", b)
print("c =", c)