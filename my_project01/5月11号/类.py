# class Car:
#     pass
#
# c1 = Car()
# c1.brand = "byd"
# print(c1.brand)
# print(c1)
# print(type(c1))
# print(c1.__dict__)

class Car:
    wheel = 4
    tax_rate = 0.1
    def __init__(self,color,brand,name,price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = float(price)
        # self.wheel = 2
    def runing(self):
        print(f"{self.brand}的{self.name}正在行驶")
    def total_cost(self, discount, rate):
        """
        计算车辆价格
        :param discount:折扣
        :param rate: 税率
        :return: 提车总费用
        """
        total_cost = self.price*discount + self.price*rate
        return total_cost
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self,other):
        return self.price == other.price and self.color == other.color and self.brand == other.brand and self.name == other.name
    def __lt__(self,other):
        return self.price < other.price

c1 = Car("red","BMW","X7","500000")
print(c1.__dict__)

c2 = Car("green","BMW","X6","450000")
print(c2.__dict__)
c2.runing()
print(c2.total_cost(0.85,0.02))

# print(c1 == c2)#基于地址进行比较
# print(c1 < c2)
# print(c1 > c2)
# print(c1)

print(c1.brand)
print(c1.wheel)