def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print ("Let's do some math with just fuctions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit type it in any way
print("Here is a puzzle.")

what = multiply(age, subtract(height, add(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
