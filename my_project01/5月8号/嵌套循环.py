#根据输入的m,n，打印长方形
m = int(input("长"))
n = int(input("宽"))
for i in range(1,n+1):
    str = ""
    for j in range(1,m+1):
        str = str + " * "
    else:
        print(str)
else:
    print("打印完成")

