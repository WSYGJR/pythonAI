#合并且去重
num_list1 = [19, 23, 54, 64 ,875, 20, 109, 232, 123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]

for num in num_list2:
    num_list1.append(num)
print(num_list1)

num_list3 = [*num_list1, *num_list2]
print(num_list3)

#去重
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(new_list)