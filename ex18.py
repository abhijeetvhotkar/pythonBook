# this one is like your scripts in the argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok that arg is just pointless we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():
    print("I got nothing")

print_two("Abhijeet", "Vhotkar")
print_two_again("Abhijeet", "Vhotkar")
print_one("First")
print_none
