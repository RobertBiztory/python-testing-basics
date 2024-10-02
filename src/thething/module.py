def f1():
    return 0

def f2():
    return 1

def f3():
    return "somestring"

def f4(a,b):
    if not isinstance(a, int):
        raise TypeError("parameter 'a' has to be an integer")
    return a+b
