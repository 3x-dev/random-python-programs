# Aryan Singhal
# 7/14/23
# Second Assignment 2nd Program

# Constants
TIP_RATE = 0.2
SALES_TAX_RATE = 0.0725


# Function to calculate the total amount
def calculate_total_amount(price, tip_rate, tax_rate):
  tip = price * tip_rate
  tax = price * tax_rate
  total_amount = price + tip + tax
  return total_amount


# Function to get the user's order
def get_order():
  first_dish = input("Enter the first food item: ")
  second_dish = input("Enter the second food item: ")
  # .lower() used for combatting case sensitivity
  return first_dish.lower(), second_dish.lower()


# Function to determine the free food given a dish order using match case statements
def get_free_food(first_dish, second_dish):
  match (first_dish, second_dish):
    case ('chicken', 'broccoli'):
      return 'ice cream'
    case ('broccoli', 'chicken'):
      return 'ice cream'
    case ('steak', 'potato'):
      return 'energy drink'
    case ('potato', 'steak'):
      return 'energy drink'
    case ('fish', 'rice'):
      return 'cupcake'
    case ('rice', 'fish'):
      return 'cupcake'
    case ('turkey', 'salad'):
      return 'cheesecake'
    case ('salad', 'turkey'):
      return 'cheesecake'
    case _:
      return 'cookie'

# Get the number of times to run the program
num_runs = int(input("Enter the number of times you want to run the program: "))

# Iterate based on the number of runs
for run in range(num_runs):
  print(f"\n\nRun #{run + 1}:")
  # Get the number of people in the group
  num_people = int(input("Enter the number of people in your group: "))
  while num_people <= 0:  # Check if the number of people is 0 or negative
    print("\nInvalid entry. Please enter a valid number of people.")
    num_people = int(input("Enter the number of people in your group: "))

  # Initialize group price
  total_price = 0
  
  # Iterate for each person
  for i in range(num_people):
    print(f"\nPerson {i + 1}:")
    valid_order = False
  
    # Loop until a valid order is entered
    while not valid_order:
      first_dish, second_dish = get_order()
  
      # Check if the entered order is valid
      valid_main_dishes = ['chicken', 'steak', 'fish', 'turkey']
      valid_side_dishes = ['potato', 'rice', 'salad', 'broccoli']
      if (first_dish in valid_main_dishes) and (
          second_dish in valid_side_dishes) and (first_dish != second_dish):
        valid_order = True
      elif (first_dish in valid_side_dishes) and (
          second_dish in valid_main_dishes) and (first_dish != second_dish):
        first_dish, second_dish = second_dish, first_dish  # Swap the dishes order
        valid_order = True
      else:
        print("\nInvalid dish order(s). Please try again.")
  
    # Dish prices
    dishes_prices = {
      'chicken': 30.25,
      'steak': 45.20,
      'fish': 37.80,
      'turkey': 38.40,
      'potato': 5.25,
      'rice': 3.10,
      'salad': 7.20,
      'broccoli': 5.25
    }
  
    first_dish_price = dishes_prices[first_dish]
    second_dish_price = dishes_prices[second_dish]
  
    # Calculate the total amount for the order
    total_amount = calculate_total_amount(
      first_dish_price + second_dish_price, TIP_RATE, SALES_TAX_RATE)
  
    # Get the free food
    free_food = get_free_food(first_dish, second_dish)
  
    # Print the order details
    print(f"\nMain Dish: {first_dish}")
    print(f"Side Dish: {second_dish}")
    print(f"Free Food: {free_food}")
    print(f"Total amount for Person {i + 1}: ${total_amount:,.2f}")
  
    # Update the total price
    total_price += total_amount
  
  # Print the total price for the group
  print(f"\nTotal price for the group: ${total_price:,.2f}")