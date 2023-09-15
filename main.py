# Baker Croyle, Sep 6, 2023, trip planner
def intro_data ():
    global First_name
    global Last_name
    global Destination
    global Days_travelling
    global Total_budget
    global Int_Days_Travelled
    global fltbudget
    global Currency_Symbol
    print("Hello, welcome to my super cool trip planner!")
    First_name = input(("Please enter your first name?"))
    Last_name = input(("Please enter your last name?"))
    print("Welcome " + First_name + Last_name)
    Destination = input(("Where would you like to go?"))
    print("Wow," + Destination + " sounds cool!")
    Days_travelling = input("how many days will you be travelling?")
    Int_Days_Travelled = int(Days_travelling)
    print(Days_travelling + " days sounds fun")
    Total_budget = input("What is your total budget for your trip in USD?")
    fltbudget = float(Total_budget)
    print("Total budget is" + Total_budget)
    Currency_Symbol = input("Please enter the currency symbol for your destination")
intro_data()

#
def converter():
# time conversions and currency conversion
    print(Currency_Symbol)
    Conversion = float(input("Please enter the conversion rate from USD to" + Currency_Symbol))
    Hours_Travelled = int(Days_travelling) * 24
    Minutes_travelled = int(Hours_Travelled) * 60
    Seconds_travelled = int(Minutes_travelled) * 60
    print("Your trip will be", Hours_Travelled, "hours!")
    print("Your trip will be", Minutes_travelled, "minutes!")
    print("Your trip will be", Seconds_travelled, "seconds!")

    # conversion for budget
    print("Your total budget for the trip is", Total_budget)
    Daily_budget = (fltbudget) / (Int_Days_Travelled)
    Rounded_daily_budget = round(Daily_budget, 2)
    print("Your daily budget is", Rounded_daily_budget)

    # conversion rate
    Destination_currency = fltbudget * Conversion
    print("your", Total_budget, "$ is now", Destination_currency, Currency_Symbol)
converter()
def valid_check():
    try:
        intro_data()
        converter()
    except:
        print("you entered an improper input")
        valid_check()
valid_check()
def time_difference():
    time_difference = int(input("Please provide the time difference as a single number. If your destinations time zone is behind, please provide a negative number"))
    time_change = (time_difference + 12)
    print("When is is Twelve O'clock at home ", "it is", time_change, "00 at your destination")
time_difference()
def area_of_country():
    area_of_country = int(input("Please provide the area of your country in kilometers squared"))
    area_in_miles = (area_of_country / 2.59)
    Rounded_area_in_miles_squared = round(area_in_miles, -1)
    print("The country you are travelling to is approximately" , Rounded_area_in_miles_squared , "square miles")
area_of_country()

