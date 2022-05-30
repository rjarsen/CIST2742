#Display a welcome message
print("===============================================================")
print("Shipping Calculator")
print("===============================================================")

#Start Loop
choice = "y"
while choice.lower() == "y":
    
    #Get user input for cost_of_item
    cost_of_item = float(input("Cost of items ordered:\t"))

       #Determine ship_cost
    if cost_of_item <= 0:
        print("You must enter a positive number. Please try again.")
        continue
    elif cost_of_item < 30:
        ship_cost = 5.95
    elif cost_of_item < 50:
        ship_cost = 7.95
    elif cost_of_item < 75:
        ship_cost = 9.95
    else:
        ship_cost = 0
    
    #Calculate total_cost and display
    total_cost = float(ship_cost + cost_of_item)
    
    if ship_cost == 0:
        print ("Shipping cost: \t\tFREE")
        print (f"Total cost: \t\t{total_cost:.2f}")
        print()
        choice = input("Continue? (y/n): ")
        print("===============================================================")      
    
    elif ship_cost != 0:
        print (f"Shipping cost: \t\t{ship_cost}")
        print (f"Total cost: \t\t{total_cost:.2f}")
        print()
        choice = input("Continue? (y/n): ")
        print("===============================================================")      
print("Bye!")