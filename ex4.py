name = 'Abhijeet Vhotkar'
age = 25
height = 74.4
weight = 180
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

# Inches to centimeter
height_in_cm = height * 2.54

# Pounds to kilogram
weight_in_kg = weight * 0.4535

print(f"Let's talk abot {name}.")
print(f"He's {height} inches tall")
print(f"Height in centimeter is {height_in_cm} cm.")
print(f"He's {weight} pounds heavy.")
print(f"Weight in kilogram is {weight_in_kg} kg.")
print("Actually thats not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# This line is tricky try to get it right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
