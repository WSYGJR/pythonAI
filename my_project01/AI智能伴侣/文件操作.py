f = open("1.txt","r",encoding="utf-8")

# content = f.read()
# print(content)
content_list = f.readlines()
for line in content_list:
    print(line.strip())

f.close()

f = open("1.txt","w",encoding="utf-8")
f.write("hello world\n")
f.write("hello world\n")
f.write("hello world\n")
f.close()