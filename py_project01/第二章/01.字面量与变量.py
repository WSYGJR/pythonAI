#字面量的写法
# print(100)  #int
# print(3.14) #float
# print(True) #bool
# print(False) #bool
# print("hello world") #str
# print("___") #str
# print(None) #NoneType空值
#
# print(True + 1)
# print(False - 1)

#变量
num = 111
print(num)
num = num + 1
print(num)

num = "ok"
print(num)

num = True
print(num)
num = False
print(num)

a = True
print("a =", a)
a = False
print("a  =", a)

#案例
#基础播放量
base = 20.7
incr = 50 #新增播放量
print("未来第一个月的播放量：", base + incr)
print("未来第二个月的播放量：", base + 2 * incr)

#一次性定义多个变量
base1,incr1 = 20.7,50
print("未来第一个月的播放量：", base1 + incr1)
print("未来第二个月的播放量：", base1 + 2 * incr1)