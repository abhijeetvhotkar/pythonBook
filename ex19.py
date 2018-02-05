def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!!")
    print(f"You have {boxes_of_crackers} boxes of crackes !!")
    print("Man thats enough for a party !!")
    print("Get a blanket.\n")

print("We can give the function numbers directly:")
cheese_and_crackers(10, 20)

print("Or we can give the variables from our script")
amount_of_cheese = 40;
amount_of_boxes = 50;

cheese_and_crackers(amount_of_cheese, amount_of_boxes)

print("We can do the math inside too")
cheese_and_crackers(10 + 20, 20 + 5)

print("We can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese + 2, amount_of_boxes + 1)
