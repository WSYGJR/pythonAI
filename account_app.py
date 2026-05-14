"""
记账程序：
1、添加收入
2、添加支出
3、查看记录
4、查看统计
5、退出
"""

import math

class Account:

    def __init__(self):
        self.income_list = []
        self.outcome_list = []
        self.total_income = 0
        self.total_outcome = 0

    def add_income(self):
        number = float(input("请输入金额："))
        type = input("请输入类型：")
        note = input("请输入备注：")
        if number is not None and type is not None and note is not None:
            temp_dic= {"金额":number, "类型":type,"备注":note}
            self.income_list.append(temp_dic)
            self.total_income += number
            print("✔添加成功")
        else:
            print("请输入正确参数")

    def add_outcome(self):
        number = float(input("请输入金额："))
        type = input("请输入类型：")
        note = input("请输入备注：")
        if number is not None and type is not None and note is not None:
            temp_dic= {"金额":number, "类型":type,"备注":note}
            self.outcome_list.append(temp_dic)
            self.total_outcome += number
            print("✔添加成功")
        else:
            print("请输入正确参数")

    def __str__(self):
        result = "收入统计：\n"
        for item in self.income_list:
            result += f"金额：{item['金额']}, 类型：{item['类型']}, 备注：{item['备注']}\n"
        result += "支出统计：\n"
        for item in self.outcome_list:
            result += f"金额：{item['金额']}, 类型：{item['类型']}, 备注：{item['备注']}\n"
        return result

    def total_account(self):
        print(f"总收入：{self.total_income}元")
        print(f"总支出：{self.total_outcome}元")
        print(f"当前余额：{self.total_income - self.total_outcome}元")

def main():
    str_note = """
记账程序：
1、添加收入
2、添加支出
3、查看记录
4、查看统计
5、退出"""

    ac = Account()
    while True:
        try:
            print(str_note)
            choice = input("请输入操作序号：")
            match choice:
                case '1':
                    ac.add_income()
                case '2':
                    ac.add_outcome()
                case '3':
                    print(ac)
                case '4':
                    ac.total_account()
                case '5':
                    print("bye~")
                    break
                case _:
                    print("请输入正确参数")
        except Exception as e:
            print(f"错误信息：{e}")


if __name__ == "__main__":
    main()
