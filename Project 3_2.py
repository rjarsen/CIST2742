#!/usr/bin/env python3

# display a welcome message
print("Tip Calculator")
print()

# get input from the user
cost = float(input("Cost of meal:\t"))

# calculate tax 15
tax_1 = cost * .15
tax_1 = round(tax_1, 2)
total_1 = float(cost + tax_1)
total_1 = round(total_1, 2)
            
# format and display the result
print()
print(f"15%")
print(f"Tip amount:\t{tax_1:.2f}")
print(f"Total amount: \t{total_1:.2f}")
print()

# calculate tax 20
tax_2 = cost * .20
tax_2 = round(tax_2, 2)
total_2 = float(cost + tax_2)
total_2 = round(total_2, 2)
            
# format and display the result
print()
print(f"20%")
print(f"Tip amount:\t{tax_2:.2f}")
print(f"Total amount: \t{total_2:.2f}")
print()

# calculate tax 25
tax_3 = cost * .25
tax_3 = round(tax_3, 2)
total_3 = float(cost + tax_3)
total_3 = round(total_3, 2)
            
# format and display the result
print()
print(f"25%")
print(f"Tip amount:\t{tax_3:.2f}")
print(f"Total amount: \t{total_3:.2f}")
print()