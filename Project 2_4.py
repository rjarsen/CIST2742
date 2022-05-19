#!/usr/bin/env python3

# display a welcome message
print("The Price Comparison Tool")
print()

# get input from the user
price_1 = float(input("Enter 1st Price: "))
oz_1 = int(input("Enter oz: "))
price_2 = float(input("Enter 2nd Price: "))
oz_2 = int(input("Enter oz: "))

# calculate price per ounce
ppo_1 = price_1 / oz_1
ppo_1 = round(ppo_1, 2)

ppo_2 = price_2 / oz_2
ppo_2 = round(ppo_2, 2)

# format and display the result
print()
print(f"Price Per oz ({oz_1} oz):\t{ppo_1}")
print(f"Price Per oz ({oz_2} oz):\t{ppo_2}")
print()

