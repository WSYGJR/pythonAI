#教务管理系统类
class IMS:
    version = "1.0"
    name = "教务管理系统"
    def __init__(self):
        self.student_list = []

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，添加失败")
                return
        math = int(input("请输入学生数学成绩："))
        eng = int(input("请输入学生英语成绩："))
        chi = int(input("请输入学生语文成绩："))
        if 0<=math<=100 and 0<=eng<=100 and 0<=chi<=100:
            stu = Student(name,math,eng,chi)
            self.student_list.append(stu)
            print("学生添加成功")
        else:
            print("成绩有误！")
    #修改学生成绩
    def update_score(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                math = int(input("请输入学生修改后数学成绩："))
                eng = int(input("请输入学生修改后英语成绩："))
                chi = int(input("请输入学生修改后语文成绩："))
                if 0<=math<=100 and 0<=eng<=100 and 0<=chi<=100:
                    s.update_score(math=math,ch=chi,eng=eng)
                    print(f"修改后的成绩{s}")
                else:
                    print("成绩错误")
        else:
            print("该学生不存在")
    #删除学生成绩
    def delete_score(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("该学生不存在")

    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息 {s}")
                return
        print("该学生不存在")

    #展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统{self.version}")

        while True:
            print("###############################################################")
            print("#1.添加学生 2.修改学生 3.删除学生 4.查询学生 5.查询所有学生 6. 退出系统# ")
            print("##############################################################")
            choice = input("请输入操作：")
            match choice:
                case"1":
                    self.add_student()
                case"2":
                    self.update_score()
                case"3":
                    self.delete_score()
                case"4":
                    self.query_student()
                case"5":
                    self.list_student()
                case"6":
                    print("bye")
                    break
                case _:
                    print("请输入正常操作")

#学生类
class Student:
    def __init__(self,name, math_score, chinese_score, english_score):
        self.name = name
        self.math_score = math_score
        self.chinese_score = chinese_score
        self.english_score = english_score

    def __str__(self):
        return f"学生名称：{self.name}，语文成绩：{self.chinese_score}，数学成绩：{self.math_score}，英语成绩：{self.english_score}"

    def update_score(self,math=None,ch=None,eng=None):
        if math is not None:
            self.math_score = math
        if ch is not None:
            self.chinese_score = ch
        if eng is not None:
            self.english_score = eng

if __name__=="__main__":
    use = IMS()
    use.run()