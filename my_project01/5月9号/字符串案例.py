#验证输入的邮箱地址
s = input("请输入邮箱")
print(s)
if s.count('@') == 1 and s.count('.') >= 1:
    print("合法")
else:
    print("非法")