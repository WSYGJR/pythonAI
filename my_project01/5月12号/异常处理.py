# try:
#     print("#"*30)
#     print(my_name)
#     print("#"*30)
#     a = 1 / 0
#
# except Exception as e:
#     print(e)
# except NameError as e:
#     print("出现name error")
# except ZeroDivisionError as e:
#     print("不允许除数为0")
# finally:
#     print("*"*30)

def func1():
    print("hello")
    func2()

def func2():
    print("world")
    func3()

def func3():
    print("yyy")
    print(my_name)

if __name__ == "__main__":
    try :
        func1()
    except  Exception as e:
        print(e)