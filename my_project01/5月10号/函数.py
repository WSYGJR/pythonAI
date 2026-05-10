import math


# def outline():
#     print("----------------")
#     return
# outline()
# outline()
# outline()
#
#
# def s_circle(radius):
#     s = 3.14 * radius**2
#     return s
#
# s1 = s_circle(5)
# print(f"面积为{s1}")

def s_rectangle(l, w):
    """
    计算长方形的面积
    :param l: 长方形的长
    :param w: 长方形的宽
    :return: 长方形的面积
    """
    area = l * w
    return area
s2 = s_rectangle(10, 5)
help(s_rectangle)
print(f"面积为{s2}")

# def cal_circle(r):
#     s = round(3.14 * r**2, 1)
#     l = round(2 * 3.14 * r, 1)
#     return s,l
# s,l = cal_circle(10)
# print(f"周长{l}，面积{s}")