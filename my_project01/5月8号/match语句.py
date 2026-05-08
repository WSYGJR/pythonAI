# day = input("请输入今天周几")
#
# match day:
#     case "1":
#         print("今天周一")
#     case "2":
#         print("今天周二")
#     case "3":
#         print("今天周三")
#     case "4":
#         print("今天周四")
#     case "5":
#         print("今天周五")
#     case "6":
#         print("今天周六")
#     case "7":
#         print("今天周日")
#     case _:
#         print("输入错误，请输入1-7")

#建议计算器
num1 = float(input("请输入第一个数字"))
num2 = float(input("请输入第二个数字"))
oper = input("请输入运算符 + - * /")
match oper:
    case "+":
        print("num1 + num2 = ",num1 + num2)
    case "-":
        print("num1 - num2 = ",num1 - num2)
    case "*":
        print("num1 * num2 = ",num1 * num2)
    case "/" if num2 != 0:
        print("num1 / num2 = ",num1 / num2)
    case _:
        print("操作不支持")
