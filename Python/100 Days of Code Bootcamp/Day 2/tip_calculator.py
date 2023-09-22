#Ioannis Apomachos
print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_per_person=(bill*(tip_percentage/100+1))/people

print(f"Each person should pay: $ {round(tip_per_person,2)}")