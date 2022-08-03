#this is to display items for their car


global total_budget




def get_budget():
    #this will collect user budget or minimum spend amount
    global total_budget
    type_of_budget = ""
    while type_of_budget not in ["budget", "non"]:
        type_of_budget = input(
            """Do you have a budget or no budget?
            Please input 'Budget' or 'non'. """)
        if type_of_budget == "budget":
            while True:
                try:
                    budget_amount = float(input("How much is your budget?"))
                    total_budget=budget_amount
                    if budget_amount > 0.0:
                        break
                except ValueError:
                    print("input a number")
        elif type_of_budget == "non":
            while True:
                try:
                    maximum_budget = float(input("What is the maximum you are willing to pay?"))
                    total_budget = maximum_budget
                    if maximum_budget > 0.0:
                        break
                except ValueError:
                    print("input a number")
                break
        break
    print("Please continue")
get_budget()
global total_budget
print(total_budget)
items = [['Wheel Lock', 92.99], ['Stering Wheel Lock', 33.99], ['GPS Tracker', 239.00]]
# it needs to print what product fits for their budget


print(items)
for i in range(len(items)):
    if total_budget >= items[i][1]:
        print("A product you can buy is {} At a price of $ {}".format(items[i][0],items[i][1]))



