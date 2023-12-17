def add(a,b):
    return a+b
def difference(a,b):
    return a-b
def product(a,b):
    return a*b
def division(a,b):
    try:
        q=a/b
    except ZeroDivisionError:
        print("Dision by Zerro")
    else:
        return q
def integerdivision(a,b):
    try:
        q=a//b
    except ZeroDivisionError:
        print("Dision by Zerro")
    else:
        return q
def remainder(a,b):
    return a%b
