a:int = 695
score:float = 80.0
hobby:str = "math"
flag:bool = False
pic:None = None

name:list[str] = ["A","b","c"]
name.append("00")
name.append(1)
print(name)

def add(a:int,b:int) -> float:
    return a+b

print(add(3,5))
print(add(3.1,55))
