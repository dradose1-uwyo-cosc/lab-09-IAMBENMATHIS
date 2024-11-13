# Benjamin Mathis
# UWYO COSC 1010
# 11/12/2024
# Lab 09
# Lab Section: 10
# Sources, people worked with, help given to: Jackson F, Austin Barner, Paige the TA
# Your
# Comments
# Here
 
# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list

class Pizza:
    """the ultimate 'za creator"""
    def __init__(self, size = 10, sauce = "tomato"):
        self.setSize(size)
        self.sauce = "tomato"
        self.toppings = ["cheese"]

    # You need to create one method that corresponds with each of the above attributes
    # which returns the corresponding attribute, just the value.
    # For the size and toppings attributes, you will need to have a method to set them.
    # - For Size, ensure it is an int > 10 (inches)
    #   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
    def setSize(self, size):
        """Checks to make sure the size entry is an integer"""
        if type(size) == int:
            pass
        elif not size.isdigit() or int(size)<10:
            self.size = 10
        else:
            self.size = int(size)
    
    def getSize(self):
        return self.size

    # - For toppings, you will need to add the toppings.
    #   - This method needs to be able to handle multiple values.
    #   - Append all elements to the list.
    #Sauce getter is bonus from Austin
    def getSauce(self):
        return self.sauce

    def setSauce(self):
        self.sauce = sauce
    
    def getToppings(self):
        return self.toppings
    
    def setToppings(self, new_toppings):
        for top in new_toppings:
            self.toppings.append(top)
    
    def getToppingsCount(self):
        return len(self.toppings)
    # Create a method that returns the amount of toppings.
    # In your __init__() method, you should take in size and sauce as parameters.
    # - Sauce should have a default value of red.
    # - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
    # Within __init__(), you will need to:
    # - Assign the parameter for size to a size attribute.
    # - Assign the parameter for sauce to the attribute.
    # - Create the toppings attribute, starting off as a list only holding cheese


#You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizzeria:
    """ that's a spighcy meat'a'ball *hand gestures*"""
    def __init__(self):
        self.orders = 0
        self.price_per_topping = 0.3
        self.price_per_inch = 0.6
        self.pizzas = []
    
    def placeOrder(self):
        entry_size = input("Please enter pizza size (mama mia): ")
        entry_sauce = input("Please enter pizza sauce, default is tomato (mama mia): ")
        beans = True
        entry_toppings = []
        while beans:
            print("enter exit to end program, if no toppings are entered only cheese will be added.")
            topping_loop = input("please enter your toppings one by one (mama mia): ")
            if topping_loop.lower() == "exit":
                beans = False
                break    
            else:
                entry_toppings.append(topping_loop)
        da_hot_stuff = Pizza(entry_size, entry_sauce)
        da_hot_stuff.setToppings(entry_toppings)
        self.pizzas.append(da_hot_stuff)
                
              
    def getPrice(self):
        pizza = self.pizzas[-1]
        return (pizza.getSize() * self.price_per_inch) + (pizza.getToppingsCount() * self.price_per_topping)
    
    def getReceipt(self):
        pizza = self.pizzas[-1]
        print(f"{pizza.getSize()}in Pizza with {pizza.getSauce()} sauce and the following toppings:")
        for y in pizza.getToppings():
            print(f"{y}")
        print("\n")
        print(f"\nSize: {pizza.getSize()}in, Base Price: ${round((pizza.getSize() * self.price_per_inch), 2)}")
        print(f"# of Toppings = {pizza.getToppingsCount()}, Price: ${round((pizza.getToppingsCount() * self.price_per_topping), 2)}")
        print(f"Total: ${round(self.getPrice(), 2)}\n\n")

    def getNumberOfOrders(self):
        if len(self.pizzas) > 0:
            return len(self.pizzas)
        else:
            return "There are no orders!"

mama_mia = Pizzeria()
active = True
while active:
    print("Would you like to place an order? Enter yes to begin or exit to exit.\n")
    begin = input()
    if begin.lower() == "exit":
        break
    elif begin.lower() == "yes":
        mama_mia.placeOrder()
        mama_mia.getReceipt()
    else:
        pass
print(f"# of Orders: {mama_mia.getNumberOfOrders()}")



# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""