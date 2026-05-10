num = 100
def print_num():
    global num
    num = 1000
    print(num)

print_num()
print(num)

def print_num2(name,age,city):
    print(f"name={name},age={age},city={city}")

print_num2("san",18,"chengdu")
print_num2(name="san",age=18,city="chengdu")
print_num2("san",age=18,city="chengdu")

def print_num3(name,age,city="chengdu"):
    print(f"name={name},age={age},city={city}")
print_num3("san",18,"chongqing")
print_num3("yi",18,)

