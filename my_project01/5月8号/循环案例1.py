#正确的用户名和密码为admin/666888,zhangsan/123456,taoge/888666
#输入用户名和密码进行登录直到登录成功
#输入的用户名和密码不能为空
#登录成功：程序结束运行，输出成功登录
#登录失败输出登录失败
correct_name1 = "admin"
correct_name2 = "zhangsan"
correct_name3 = "taoge"
correct_password1 = "666888"
correct_password2 = "123456"
correct_password3 = "888666"
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "" or password == "":
        print("用户名和密码不能为空")
    if username == correct_name1 and password == correct_password1:
        print("登录成功")
        break
    elif username == correct_name2 and password == correct_password2:
        print("登录成功")
        break
    elif username == correct_name3 and password == correct_password3:
        print("登录成功")
        break
    else:
        print("登录失败")
