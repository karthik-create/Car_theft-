#This is for the introduction and Asking user info
#Asking user their name and checking if it is correct
def name():
    name_1=input("What is your name?")
    right_name=input("Your name is {}. Is this correct? press [y/n]".format(name_1))
    if right_name == 'y':
        print("Hi {}. Welcome to my Car theft prevention app.".format(name_1))
    else:
        right_name_2 = input("Please enter your correct name.")
        print("Hi {}. Welcome to my Car theft prevention app.".format(right_name_2))


name()