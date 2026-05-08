length = int(input("请输入直角边边长"))
for i in range(1,length+1):
    for j in range(1,i+1):
        print("*",end="\t")
    else:
        print()

num = int(input("请输入数字"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f"{j}",end="\t")
    else:
        print()

for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
            print("■",end="\t")
        else:
            print("▢",end="\t")
    else:
        print()