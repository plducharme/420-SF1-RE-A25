def fonction():
    global b
    print("premier print() fonction: b=", b)
    a = 3
    c = 5
    b = b + c
    print("deuxième print() fonction: b=", b)
    print("print() fonction: a=", a)
    return a


a = 2
b = 2
print("print() avant la fonction: a=", a)
print("print() avant la fonction: b=", b)
fonction()
print("print() après la fonction: a=", a)
print("print() après la fonction: b=", b)
