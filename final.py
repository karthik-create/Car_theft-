# here is where my def starts
def name():
    # This is for the introduction and Asking user info
    # Asking user their name and checking if it is
    # correct and welcomes user to the app
    name_1 = input("What is your name?")
    right_name = input("Your name is {}. Is this correct? press [y/n]".format(name_1.title()))
    if right_name == 'y':
        print("Hi {}. Welcome to my Car theft "
              "prevention app.".format(name_1.title()))
    else:
        right_name_2 = input("Please enter your correct name.")
        print("Hi {}. Welcome to my Car theft "
              "prevention app.".format(right_name_2.title()))


def car_detail():
    ''' here the app will be asking the user for the brand, model and year of
    their car and telling them accessories are universal and can be used
    for 99% of common cars unlike indy cars'''
    car_brands = ["toyota", "subaru", "nissan", "honda"]
    car_brand = input("What is your Car brand? ")
    if car_brand not in car_brands:
        car_brand = input("Please enter a car brand "
                          "from the list {}".format(car_brands))
    else:
        print("PLease continue")

    car_model = input("What is the model of your car ?")

# Here the purpose of the code is for the year to be a number not words
    try:
        car_yr = int(input("What year is your car"))
        if 2022 >= car_yr >= 1998:
            print("Please continue")
        else:
            car_yr = int(input(" Please enter a  year between 1898 and 2022"))
    except ValueError:
        car_yr = int(input("what year is your car (In Numbers PLease)"))
        if 2022 >= car_yr >= 1998:
            print("Please continue")
        else:
            car_yr = int(input("Please enter a  year between 1898 and 2022"))

    car_info = input("Your car is a {} {} {}. "
                     "Is this correct? press [y/n]"
                     .format(car_brand.title(), car_model.title(), car_yr))
    if car_info == 'y':
        car_select = input("You will be searching for "
                           "universal accessories for a {} {} {} to "
                           "prevent theft. Press enter to"
                           " continue".format(car_brand.title(),
                                              car_model.title(), car_yr))
    else:

        print("Please enter the correct "
              "details of your car")
        car_brand = input("What is your Car brand? ")
        if car_brand not in car_brands:
            car_brand = input("Please enter a car "
                              "brand from the list {}".format(car_brands))
        else:
            print("PLease continue")
        car_model = input("What is the model of you car? ")
        car_yr = int(input("What is the year of you car? "))
        car_select = input(
            "You will be searching for accessories for "
            "{} {} {} to prevent theft."
            .format(car_brand.title(), car_model.title(), car_yr))


global total_budget
# Here I have made the variable 'total_budget' global
# so it can be used throughout the code


def get_budget():
    # this will collect user budget or
    # maximum amount they would like to spend
    global total_budget
    type_of_budget = ""
    # this asks the user their budget and makes sure it is more than 0
    while type_of_budget not in ["budget", "non"]:
        type_of_budget = input(
            """Do you have a budget or no budget?
            Please input 'Budget' or 'non'. """)
        if type_of_budget == "budget":
            while True:
                try:
                    budget_amount = float(input("How much is your budget?"))
                    total_budget = budget_amount
                    if budget_amount > 0.0:
                        break
                except ValueError:
                    print("input a number")
        elif type_of_budget == "non":
            while True:
                try:
                    maximum_budget = float(input("What is the"
                                                 " maximum you are"
                                                 "willing to pay?"))
                    total_budget = maximum_budget
                    if maximum_budget > 0.0:
                        break
                except ValueError:
                    print("input a number")
                break
        break
    print("Please continue")

# main starts here
run_again = input("Please press"
                  " <Enter> to start").lower()

while run_again == "":
    name()
    car_detail()
    get_budget()
    global total_budget
    print("your budget is $ {}".format(total_budget))
    items = [['Wheel Lock', 92.99],
             ['Steering Wheel Lock', 33.99],
             ['GPS Tracker', 239.00]]
    # it needs to print what product fits for their budget
    if total_budget >= 33.99:
        for i in range(len(items)):
            if total_budget >= items[i][1]:
                print("A product you can buy is {}"
                      "At a price of $ {}"
                      .format(items[i][0], items[i][1]))
        run_again = input(" Press <Enter> to start again"
                          "or 'xxx' to end").lower()
        if run_again == 'xxx':
            print("Thank You for using my app and hope you got"
                  "an accessory you were looking for.")
            print("Hope to see you again")
    else:
        run_again == 'xxx'
        print("Sorry You do not have enough money to purchase any accessories")

    for i in range(len(items)):
        if total_budget >= items[i][1]:
            print("A product you can buy is {}"
                  "At a price of $ {}".format(items[i][0], items[i][1]))
    run_again = input(" Press <Enter> to start again or 'xxx' to end").lower()
    if run_again == 'xxx':
        print("Thank You for using my app and hope you got"
              "an accessory you were looking for.")
        print("Hope to see you again")
