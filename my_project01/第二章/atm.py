true_password = 111111
total = 10000
password = input("请输入密码")
if password == str(true_password):
    get_num = input("请输入取款金额")
    if (total - int(get_num)) < 0:
        print("余额不足")
    else:
        total = total - int(get_num)
        print(f"余额{total}")
else:
    print("密码错误")