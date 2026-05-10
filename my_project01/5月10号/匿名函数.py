out_line = lambda : print('---------------')
add = lambda x,y:x+y
out_line()
print(add(10,20))


data_list = ["C++","C","Python","Java","PHP","Go","Rust","C#"]
print(data_list)

data_list.sort(key=lambda item:len(item),reverse=False)
print(data_list)
data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)
