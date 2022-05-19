#!/usr/bin/env python3

# Display message
print("Registration Form.")
print()

# Input from user
f_name = (input("Enter First Name:\t"))
l_name = (input("Enter Last Name:\t"))
b_day = (input("Enter year of Birth:\t"))

# Display and create temp PW
print()
print(f"Welcome {f_name} {l_name}!")
print(f"Your registration is complete.")
print(f"Your Temporary Password is: {f_name}*{b_day}")
print()