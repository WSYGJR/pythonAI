__all__ = ["PI", "log_seperate3"]
PI = 3.1415926
NAME = "YSJ"

def log_seperate1():
    print("-"*30)

def log_seperate2():
    print("+"*30)

def log_seperate3():
    print("#"*30)

def log_seperate4():
    print("*"*30)

def s(radius:float)->float:
    return PI*radius**2

def l(radius:float)->float:
    return PI*radius*2

#执行当前文件，则会执行如下代码；如果被当作模块导入，则如下代码不执行
if __name__ == '__main__':
    log_seperate1()
    log_seperate2()