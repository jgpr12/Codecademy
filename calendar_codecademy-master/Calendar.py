""" In this project, we'll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event"""

from time import sleep, strftime

USER = 'Jose'
calendar = {}

def welcome():
  print "Welcome to your calendar, " + USER
  print "Opening calendar..."
  sleep(1)
  print strftime("%A %B %d, %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    print "Enter the following options:\n",\
    "A to Add\nU to Update\nV to View\n",\
    "D to Delete\nX to Exit"
    option = raw_input("Option: ").upper()
    
    # Perform actions based on the choice
    if option == "V":
      if len(calendar.keys()) == 0:
        print "Empty calendar"
      else:
        print calendar
    elif option == "U":
      date = raw_input("What date?")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update succesful..."
    elif option == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(strftime("%Y")) > int(date.split('/')[2]):
        print "Invalid date entered..."
        try_again = raw_input("Try again? Y for yes, N for No: ").upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event added succesfully..."
        print calendar
    elif option == "D":
      if len(calendar.keys()) == 0:
        print "Empty calendar..."
      else:
        event = raw_input("What event? ")
        for date in calendar:
          if calendar[date] == event:
            del calendar[date]
            print "Event deleted..."
            break
        else:
          print "Invalid event..."
    elif option == "X":
      start = False
    else:
      print "Invalid Command..."
      start = False
start_calendar()