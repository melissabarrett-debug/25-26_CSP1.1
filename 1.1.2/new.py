# import the datetime module to get the current date/year
import datetime as dt

# ask user for their name then welcome them
bob= input("What is your name?")
print("Hello","bob", "welcome to my program.")

# ask user for their age
#14= input("How old are you?")

# get the current year using the datetime object that resides in the datetime module
curr_year = dt.datetime.now().year

# prepare and display output
birth_year = curr_year -int(14)
print("Hmmm... were you born in","2011", "2011")