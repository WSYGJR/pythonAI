dict2 = {"王琳":670,"利姆湾":608,"蓄力过":580,"王琳":700}
dict2["123"] = 123
print(dict2)

dict2["123"] = 456
print(dict2)

dict2.pop("123")
print(dict2)
del dict2["蓄力过"]
print(dict2)
print(dict2.values())
print(dict2.items())
print(dict2.keys())
print(dict2.get("王琳"))
print(dict2["王琳"])

for k in dict2.keys():
    print(f"{k}: {dict2[k]}")
for k,v in dict2.items():
    print(f"{k}: {v}")