def cal(x):
    if x>0:
        return x*cal(x-1)
    else:
        return 1
print(cal(10))