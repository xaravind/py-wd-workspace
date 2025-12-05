# Import Statements
# Constant Definitions
# Function definitions
# Function
# m = 100
def display():
    print("I am a display Function")

def add(a,b):
    # global m
    # m = 75
    # print(f"The value of a is", m)
    return a + b

def wrapper():
    m = 100
    print("The value of m inside wrapper is",m)
    def func1():
        nonlocal m
        m = 25
        n = 75
        print("The value of n is",n)
        print("The value of m inside func1 is",m)
    
    func1()
    print("The value of m inside wrapper is",m)


display()
# print(f"The value of a is", m)
# print(f"The sum is {add(9,10)}")
# print(f"The value of a is", m)
wrapper()

