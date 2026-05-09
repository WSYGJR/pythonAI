todo_list = []
while True:
    print("请选择增加 or 删除 事项----0：增加，1：删除，其他：退出")
    num = input()
    if num == "0":
        todo_list.append(input("请输入代办事项"))
    elif num == "1":
        index = 0
        print("请输入要删除的事项id")
        for i in todo_list:
            print(f"{index}\t{i}")
            index += 1
        delete = int(input())
        todo_list.remove(todo_list[delete])
        print(todo_list)
    else:
        break
