months = {"January": 31,

          "March": 31,

          "April": 30,

          "May": 31,

          "June": 30,

          "July": 31,

          "August": 31,

          "September": 30,

          "October": 31,

          "November": 30,

          "December":31

}

month = input("Enter the ame of month: ")

if month == 'February':

    print("There are 28 or 29 days in {}".format(month))

elif month in months:

    print("There are {} days in {}".format(months[month],month))

else:

    print("Check your spelling or this is not a month")