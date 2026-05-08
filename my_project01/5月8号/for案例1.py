#计算1-100之内的奇数和
#计算100-500之间所有3的倍数的数字之和
sum1 = 0
for i in range(1,101):
    if i % 2 == 1:
        sum1 += i
else:
    print("1-100之间所有奇数和为：",sum1)

sum2 = 0
for i in range(100,501):
    if i % 3 == 0:
        sum2 += i
else:
    print("100-500之间所有3的倍数的数字和为：",sum2)

sum3 = 0
for i in range(1, 101, 2):
    sum3 += i
else:
    print("1-100之间所有奇数和为：",sum3)

sum4 = 0
for i in range(102, 501, 3):
    sum4 += i
else:
    print("100-500之间所有3的倍数的数字和为：",sum4)