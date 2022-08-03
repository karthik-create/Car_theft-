
def car_detail():
    car_brand = input("What is your Car brand? ")
    car_model = input("What is the model of you car? ")
    car_yr = int(input("What is the year of you car? "))
    if car_yr <= 2022 and car_yr>=1998 :
        print("Please Continue")
    else:
        print("Please enter your cars correct year between 1898 and 2022")
        car_yr = int(input("What is the year of you car? "))


    car_info = input("Your car is a {} {} {}. Is this correct? press [y/n]".format(car_brand.title(), car_model.title(), car_yr))
    if car_info == 'y':
        car_select = input("You will be searching for universal accessories for  a {} {} {} to prevent theft. Press enter to continue".format(car_brand.title(), car_model.title(), car_yr))
    else:
        print("Please enter the correct details of your car")
        car_brand = input("What is your Car brand? ")
        car_model = input("What is the model of you car? ")
        car_yr = int(input("What is the year of you car? "))
        car_select = input("You will be searching for accessories for {} {} {} to prevent theft.".format(car_brand.title(), car_model.title(), car_yr))















car_detail()


