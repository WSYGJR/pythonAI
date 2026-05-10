def funca():
    print("hello a")
    funcb()
    print("bye a")

def funcb():
    print("hello b")
    funcc()
    print("bye b")

def funcc():
    print("ccc")

funca()
