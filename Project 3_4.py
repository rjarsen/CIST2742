#!/usr/bin/env python3

# display a welcome message
print("===============================================================")
print("Shipping Calculator")
print("===============================================================")

# create loop
choice = "y"
while choice.lower() == "y":
    
    # get user input for coi
    coi = float(input("Cost of items ordered:\t"))
    
    # conduct calculation, display results, ask if user wants to continue
    if coi > 75:
        tc = coi
        print ("Shipping cost: \t\tFREE")
        print (f"Total cost: \t\t{tc:.2f}")
        print ()   
        choice = input("Continue? (y/n): ")
        print("===============================================================")
    elif coi >= 50:
        sc = 9.95 
        tc = float(sc + coi)
        print ("Shipping cost: \t\t9.95")
        print (f"Total cost: \t\t{tc:.2f}")
        print()
        choice = input("Continue? (y/n): ")
        print("===============================================================")        
    elif coi >=30:
        sc = 7.95 
        tc = float(sc + coi)
        print ("Shipping cost: \t\t7.95")
        print (f"Total cost: \t\t{tc:.2f}")
        print()
        choice = input("Continue? (y/n): ")
        print("===============================================================")        
    elif coi >= 0:
        sc = 5.95 
        tc = float(sc + coi)
        print ("Shipping cost: \t\t5.95")
        print (f"Total cost: \t\t{tc:.2f}")
        print ()
        choice = input("Continue? (y/n): ")
        print("===============================================================")        
    elif coi < 0:
        print("You must enter a positive number. Please try again.")
print("Bye!")
    