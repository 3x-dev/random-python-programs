# Aryan Singhal
# August 7, 2023
# Final Project

# Summer Camp Activities Registration System
# Description: This summer camp registration system allows users to easily explore and register in various camp activities. The user can browse through all the available activities, sign up for the ones the user is interested in, check their availability, and exit the registration system as needed. The camp offers a total of four activities: basketball, swimming, dance, and art. Basketball and swimming fall under the "sport activities" category and initially provide 10 open spots each for registration. On the other hand, dance and art are classified as "creative activities" and start with only 5 available spots each. The system efficiently tracks the number of registrations for each activity as well as the remaining spots using text file manipulation. To successfully register for an activity, the user just needs to provide the individual's name who wishes to participate and the desired activity name (case insensitive). If an activity reaches its maximum capacity, the user won't be able to register for it, and the user will receive a prompt to choose another activity with available spots.

# Constants
MAX_PARTICIPANTS_SPORT = 10  # Maximum number of participants for sports
MAX_PARTICIPANTS_CREATIVE = 5  # Maximum number of participants for creative activities


# Function #1 to display the main menu
def display_menu():
  # Displays the main menu options for the registration system
  print("\nAryan's Summer Camp Registration Dashboard:")
  print("1 - Display camp activities and respective status")
  print("2 - Register for an activity")
  print("3 - Check number of spots available for an activity")
  print("4 - Exit camp registration system")


# Function #2 to display the available activities and their status (FULL or AVAILABLE)
# param activities: A dictionary containing activity names and maximum participant counts.
#
# Reading file using "with" keyword
# Using FOR loop to iterate through a dictionary
def display_activities(activities):
  print("\nCamp Activities:")
  for activity in activities:  # For loop
    file_name = f"{activity}_signups.txt"
    with open(file_name, "r") as file:
      lines = file.readlines()
      print(f"# Reading {file_name} file")
      if len(lines) == activities[activity]:
        print(activity.upper() + " - FULL")
      else:
        print(activity.upper() + " - AVAILABLE")


# Function #3 to register a participant for an activity
# param activity: The activity for which the participant is being registered.
# param activities: A dictionary containing activity names and maximum participant counts.
# param name: The name of the participant being registered.
#
# Reading AND Appending to a file using "with" keyword and open/close methods respectively
def sign_up(activity, activities, name):
  if activity in activities:
    file_name = f"{activity}_signups.txt"
    with open(file_name, "r") as file:
      lines = file.readlines()
      print(f"# Reading {file_name} file to make sure spots are open")
      if len(lines) < activities[activity]:
        handle = open(file_name, "a")
        handle.write(f"{name} has registered for {activity}\n")
        handle.close()
        print(
          f"\nSuccessfully registered {name} for {activity}! {name}'s registration has been added to the {file_name} file."
        )
      else:
        print(
          f"\nSorry, no available spots for {activity}. Please choose another activity."
        )
  else:
    print(
      "\nInvalid activity name. Valid activities to choose from: Basketball, Swimming, Dance, Art. Please try again.\n"
    )


# Function #4 to check and display the number of available spots for a specific activity
# param activity: The activity for which to check available spots.
# param activities: A dictionary containing activity names and maximum participant counts.
def check_spots(activity, activities):
  if activity in activities:
    file_name = f"{activity}_signups.txt"
    print(f"# Reading {file_name} file")
    with open(file_name, "r") as file:
      lines = file.readlines()
      available_spots = activities[activity] - len(lines)
      print(
        f"\nNumber of spots available for {activity}: {available_spots}/{activities[activity]}"
      )
  else:
    print(
      "\nInvalid activity name. Valid activities to choose from: Basketball, Swimming, Dance, Art. Please try again."
    )


# Main function to run the program
#
# Using if…elif…else statements while accepting user input
def main():

  # Using Dictionary - Initialize the activities dictionary with respective maximum participant counts
  activities = {
    "basketball": MAX_PARTICIPANTS_SPORT,
    "swimming": MAX_PARTICIPANTS_SPORT,
    "dance": MAX_PARTICIPANTS_CREATIVE,
    "art": MAX_PARTICIPANTS_CREATIVE
  }

  choice = True
  while choice:  # WHILE loop
    display_menu()
    choice = input("\nPlease choose an option (1, 2, 3, or 4): ")

    # If..elif..else statements
    if choice == "1":  # Display activities
      display_activities(activities)
    elif choice == "2":  # Register individual for an activity
      name = input(
        "\nPlease provide the name of the individual you wish to register for the activity (enter 'cancel' to cancel registration): "
      )
      if name.lower() == "cancel":
        print("\nAction cancelled!")
      else:
        reg_done = False
        while not reg_done:
          activity = input(
            "Please provide the desired activity name you want to register for (enter 'cancel' to cancel registration): "
          )
          activity = activity.lower()  # Case insensitive
          if activity == "cancel":
            print("\nAction cancelled!")
            reg_done = True
          else:
            if activity in activities:
              file_name = f"{activity}_signups.txt"
              with open(file_name, "r") as file:
                lines = file.readlines()
                if len(lines) == activities[activity]:
                  print(
                    f"\nSorry, no available spots for {activity}. Please choose another activity.\n"
                  )
                else:
                  sign_up(activity, activities, name)
                  reg_done = True  # Exit the loop after a successful sign-up
            else:
              print(
                "\nInvalid activity name. Valid activities to choose from: Basketball, Swimming, Dance, Art. Please try again.\n"
              )
    elif choice == "3":  # Check available spots for an activity
      spot_choice = True
      while spot_choice:
        activity = input(
          "\nPlease provide the desired activity name you want to check spots for (enter 'cancel' to cancel): "
        )
        activity = activity.lower()  # Case insensitive
        if activity == "cancel":
          print("\nAction cancelled!")
          spot_choice = False
        else:
          check_spots(activity, activities)
    elif choice == "4":  # Exit the program
      print("\nExiting Aryan's camp registration system. Thank you!")
      choice = False
    else:
      print("\nInvalid choice! Please try again.")


# Program entry point
print("1. Dictionary -- line 95\n\n")
print("Hello! Welcome to Aryan's Summer Camp Registration System.")
main()  # Call the main function to start the program
