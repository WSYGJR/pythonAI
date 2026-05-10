#选修足球学生名单
football_set={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set={"许木","王卓","十三","虎跑","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
#选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

s = french_set.intersection(art_set)
print(f"选修了法语和艺术的学生{s}")

s2 = french_set & art_set
print(f"选修了法语和艺术的学生{s2}")

all_set = french_set & art_set & football_set & basketball_set
print(f"同时选修了四门的学生：{all_set}")

s3 = football_set.difference(basketball_set)
print(f"选修了足球但是没有选秀篮球的学生{s3}")
s4 = football_set - basketball_set
print(f"选修了足球但是没有选秀篮球的学生{s4}")
s5 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球但是没有选秀篮球的学生{s5}")

all_name = football_set | basketball_set | french_set | art_set
print(f"所有学生{all_name}")
all_list = [*football_set, *basketball_set, *french_set, *art_set]
for item in all_name:
    print(f"{item}选修了{all_list.count(item)}课程")


