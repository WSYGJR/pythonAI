def calculate(*args):
    print(args)

calculate(1,2,3,4)
calculate(1,2,3,4,5,6,7,8,9)

def cc(**kwargs):
    print(kwargs)

cc(count=1,c1=3,hgaiso=777)
def add(x,y):
    return x+y
def cal(x,y,oper):
    return oper(x,y)

print(cal(10,20,add))