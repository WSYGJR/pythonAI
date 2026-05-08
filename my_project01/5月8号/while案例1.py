#计算1-100之间的所有偶数的累加之和
i = 0
sum = 0
while i < 101:
    if i % 2 == 0:
        sum = sum + i
    i += 1
else:
    print("1-100之间所有偶数的累加和为",sum)