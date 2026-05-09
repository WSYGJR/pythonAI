list1 = []
for i in range(1,11):
    list1.append(int(input("请输入数字")))
list1.sort()
print("最小值",list1[0])
print("最大值",list1[9])
print("平均值",sum(list1)/len(list1))
print(list1)