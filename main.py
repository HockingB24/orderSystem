# Get input from CLI arguments using 'sys'
import sys
from src.orderSystem import OrderSystem

# Main function takes in input arguments and prints order 
def main(args):
    # Make sure there are enough arguments -- if not, throw errors immediately based on what is missing
    numArgs = len(args)
    if numArgs == 0:
        print("Unable to process: Meal and Order are missing")
        return
    if numArgs == 1:
        # If the input argument's first char is a number, the order is there but the meal is missing
        if args[0][0].isnumeric(): 
            print("Unable to process: Meal is missing")
            return 
        # If the input argument's first char is in the alphabet, it is most likely the meal name
        elif args[0][0].isalpha():
            # Add missing items from order based on the meal inputted 
            errString = "Unable to process: Main is missing, side is missing"
            if args[0] == "Dinner":
                errString += ", dessert is missing"           
            print(errString)
            return 
    
    meal = args[0]

    # Split the order from CSV's to a sorted list
    # It is sorted because our output order should always be Main Course, Side, Drink, Dessert (1, 2, 3, 4)
    order = args[1]
    order = order.split(',')
    order.sort()

    orderSystem = OrderSystem()
    # Give the orderSystem our order 
    myOrder = orderSystem.orderMeal(meal, order)
    
    # orderMeal() will return None if the order is invalid. If it doesn't, print order 
    if myOrder != None:
        print(myOrder)
    
if __name__ == "__main__":
    main(sys.argv[1:])
