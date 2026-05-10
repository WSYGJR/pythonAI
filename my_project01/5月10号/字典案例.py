#购物车系统，增删改查
#
dict1 = {"mate80":{"price":6999,"num":2},"water":{"price":10,"num":1000}}

while True:
    print("""
          ###########购物车系统##########
          #         1.添加购物车        #
          #         2.修改购物车        #
          #         3.删除购物车        #
          #         4.查询购物车        #
          #         5.推出购物车        #
          #############################
          请选择要执行的操作(1-5):
          """)
    num = input()
    match num:
        case "1":
            print("请输入商品名称")
            name = input()
            if name in dict1.keys():
                print("该商品已存在")
                continue
            print("请输入商品价格")
            price = input()
            print("请输入商品数量")
            num = int(input())
            dict1[name] = {"price":price,"num":num}
            print(dict1.items())
        case "2":
            print(dict1.items())
            print("请选择修改的商品")
            name = input()
            if name not in dict1.keys():
                print("该商品不存在")
                continue
            print("请输入商品价格")
            price = input()
            print("请输入商品数量")
            num = int(input())
            dict1[name] = {"price": price, "num": num}
            print(dict1.items())
        case "3":
            print(dict1.items())
            print("请选择删除的商品")
            name = input()
            if name not in dict1.keys():
                print("该商品不存在")
                continue
            dict1.pop(name)
            print(dict1.items())
        case "4":
            print("请输入查询的商品")
            name = input()
            if name in dict1.keys():
                print(dict1.get(name))
            else:
                print("商品不存在")
        case "5":
            break
        case _:
            print("请输入正常操作")