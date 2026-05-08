#模拟B站账号密码登录
correct_id = "123456789"
correct_password = "123456ysj"
input_id = input("请输入账号")
input_password = input("请输入密码")
if input_id == correct_id and input_password == correct_password:
    print("登录成功")
else:
    print("账号和密码不一致")