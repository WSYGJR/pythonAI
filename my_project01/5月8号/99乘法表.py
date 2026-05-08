str1 = ""
for i in range(1,10):
    for j in range(1,i+1):
        str1 += f"{j} x {i} = {i*j}    "
    else:
        print(str1)
        str1 = ""

