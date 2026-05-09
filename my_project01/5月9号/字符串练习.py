#判断回文
s1 = "黄山落叶松叶落山黄"
s2 = "上海自来水来自海上"
for i in range(0,int(len(s1)/2)):
    if s1[i] != s1[-i-1]:
        print("不是回文")
        break
else:
    print("回文")

for i in range(0,int(len(s2)/2)):
    if s2[i] != s2[-i-1]:
        print("不是回文")
        break
else:
    print("回文")

s3 = []
for i in range(0,10):
    s3.append(input("请输入字符串"))
for s in s3:
    print(s)