# Creating user input for cost of food, number of people splitting the bill and percentage of the tip.

cost_of_food = input("How much does the food cost?")
num_of_people = input("How many people are splitting bill?")
tip_percentage = input("What percentage would you like to tip?")

#Turn input into integers so that we can write formulas for determining the total bill and how much each person should pay. We're choosing to use float over int, so that the bill can reflect change and not rounding bill to only whole numbers.

cost = float(cost_of_food)
people = float(num_of_people)
tip = float(tip_percentage)

#Formula to divide the tip input by 100 so that when we multiply the tip with the cost we can get an accurate percentage of tip.
percentage = tip/100

#Formula to determine how much in tip we are giving 

how_much_in_tips = cost * percentage 

#Forula to determine total cost including tax

total_cost = cost + how_much_in_tips

#Formula to determine whats the cost to each person 
split_cost = total_cost / people

print(f"The total bill comes out to ${total_cost} and each person has to pay ${split_cost}")

