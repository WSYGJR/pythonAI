def s_triangle(d, h):
    return d*h/2

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

def count_h_l_a(s):
    print(f"最高分{max(s)},最低分{min(s)}，平均分{sum(s)/len(s)}")

s1 = s_triangle(10,20)
print(f"三角形面积为{s1}")
s2 = count_vowels("ghuasihgiwnvuihaiognoabjNUAHGIUFDSF")
print(f"共计有{s2}个元音字母")
count_h_l_a([1235,154,123,789,134546,146,456])