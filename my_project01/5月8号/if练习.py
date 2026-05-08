#奇数偶数
#成年
#正负（不考虑0）
#及格
num = int(input("请输入一个整数"))
age = int(input("请输入年龄"))
score = int(input("请输入考试分数"))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")
if age >= 18:
    print("成年")
else:
    print("未成年")
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("0")
if score >= 60:
    print("及格")
else:
    print("不及格")