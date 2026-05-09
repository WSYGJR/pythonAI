num_list = []
for i in range(1,21):
    num_list.append(i**2)
print(num_list)

num_list2 = [i**2 for i in range(1,21)]
print(num_list2)

num_list1 = [19, 23, 54,64,87,20,109,232,123,4,26,55,72]
new_list = []
for num in num_list1:
    if num % 2 == 0:
        new_list.append(num**2)
print(new_list)

new_list1 = [i**2 for i in num_list1 if i%2==0]
print(new_list1)
