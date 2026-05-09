#根据提供的学生成绩单完成需求
#需求1：计算每个学生的总分、各科平均分,一并输出
#统计各科成绩最低分,最高分,平均分,并输出
#查找成绩优秀的学生,平均分大于90的学生,并输出
from 第二章.atm import total

students = (
    ("S001", "王林",85,92,78),
    ("S002", "LI", 92, 88, 85),
     ("S003","十三",78,85,82),
     ("S004","营牛",88,79,91),
    ("S005","周轶",95,96,89),
    ("S006","王卓",76,82,77),
     ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
     ("S009","许木",86,89,98),
     ("S010","道天",66,59,72)
)

for s in students:
    total = sum(s[2:5])
    avg = total / 3
    print(f"{s[0]} {s[1]} {s[2]} {s[3]} { s[4]} {total} {avg:.1f}")

for id,name,chinese1,math1,english1 in students:
    print(f"{id}\t{name}\t{chinese1}\t{math1}\t{english1}")
math = [s[3] for s in students]
chinese = [s[2] for s in students]
english = [s[4] for s in students]
print(f"语文最低分：{min(chinese)}，最高分：{max(chinese)}，平均分：{sum(chinese)/len(chinese)}")
print(f"数学最低分：{min(math)}，最高分：{max(math)}，平均分：{sum(math)/len(math)}")
print(f"英语最低分：{min(english)}，最高分：{max(english)}，平均分：{sum(english)/len(english)}")

print("优秀学生")
for s in students:
    total = sum(s[2:5])
    avg = total / 3
    if avg > 90:
        print(f"{s[0]} {s[1]} {s[2]} {s[3]} {s[4]} {total} {avg:.1f}")
