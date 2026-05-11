#导入模块   通过模块名.功能名\别名.功能名调用
# import random
#
# for i in range(100):
#     print(random.randint(1,100))
#
# import random as rnd
# for i in range(10):
#     print(rnd.randint(0,100))


#导入模块中的功能     调用方式：功能名\别名
# from random import randint
# for i in range(10):
#     print(randint(0,100))

from random import randint as rint
print(rint(1,100))