# name = "bro"


# def display():
#     name = "Code"
#     print(name)


# display()
# print(name)


# ARGS

def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
        return sum


print("Answer:")
print(add(5, 2, 3))
