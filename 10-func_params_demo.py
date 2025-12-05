
def my_function(param1, param2, username="Guest", city="Unknown"):
    """A simple function that takes two parameters and returns their sum."""
    return f"User {username} from {city} is having the amount: {param1 + param2}"

print(my_function(10,20,city="pune", username="vishwas"))

def add(*args):
    """Function to add any number of arguments."""
    return sum(args)

print(add(1,2,3,4,5,6,7,8,9,10,25,30))


def user_info(**kwargs):
    """Function to display user information."""
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="vishwas",city="pune",country="India")

# generate 10 Numbers in a list
l1 = []
for i in range(10):
    l1.append(i)

print(l1)

l1 = [x for x in range(10)]
l2 = [x**2 for x in range(10)]

fn = lambda x: x**2

# list of names
names = ["vishwas",'Bob',"jan","jane"]
# new_names = []
# for name in names:
#     if (len(name) < 4):
#         new_names.append(name)

new_names = filter(lambda name: len(name) < 4, names)
