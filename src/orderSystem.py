# This OrderSystem class stores a menu and the types of items on the menu, and 
# allows us to access the public orderMeal() function. 
class OrderSystem:
    # Create OrderSystem variables for the menu and the types of items on the menu
    # Types of items are in the same order as they appear on the menu, so we can 
    # take advantage of indexing
    _menu = {
                "Breakfast": ["Eggs",     "Toast",    "Coffee", None],
                "Lunch":     ["Sandwich", "Chips",    "Soda",   None],
                "Dinner":    ["Steak",    "Potatoes", "Wine",   "Cake"]
    }
    _itemTypes = ["Main", "Side", "Drink", "Dessert"]

    # Constructor for OrderSystem
    # Doesn't take any variables -- the menu is already defined
    def __init__(self):
        pass
    
    # Checks if order is valid. If not, prints error and returns "None". If it is, it returns the valid order.
    # Note: Since water is always provided at dinner, this function adds water to dinner orders.
    def __checkOrder(self, meal, ordersWithTypes):
        errString = ""
        typesOfOrders = ordersWithTypes["Types"]
        itemsOrdered = ordersWithTypes["Orders"]

        # Accumulate the number of each meal
        numOfType = {"Main": 0, "Side": 0, "Drink": 0, "Dessert": 0}
        for type in typesOfOrders:
            if type in numOfType:
                numOfType[type] += 1
        # Check for errors related to the number of each meal 
        if numOfType["Main"] == 0:
            errString += "Main is missing. "
        if numOfType["Side"] == 0:
            errString += "Side is missing. "
        if meal == "Dinner" and numOfType["Dessert"] == 0:
            errString += "Dessert is missing. "

        # Make booleans for other, general error conditions - order is invalid if any are met. 
        multipleSidesNotLunch = (numOfType["Side"] > 1 and meal != "Lunch")
        tooManyMainCourses = numOfType["Main"] > 1 
        multipleDrinksNotBreakfast = (numOfType["Drink"] > 1 and meal != "Breakfast")

        # Handle the general errors (Sequentially so all errors can be caught)
        if multipleSidesNotLunch :
            numIndex = typesOfOrders.index("Side")
            errString += itemsOrdered[numIndex] + " can not be ordered more than once. "
        if tooManyMainCourses:
            numIndex = typesOfOrders.index("Main")
            errString += itemsOrdered[numIndex] + " can not be ordered more than once. "
        if multipleDrinksNotBreakfast:
            numIndex = typesOfOrders.index("Drink")
            errString += itemsOrdered[numIndex] + " can not be ordered more than once. "

        # Add water if meal is dinner OR meal doesn't include a drink
        if meal == "Dinner":
            itemsOrdered.insert(-1, "Water")
        elif numOfType["Drink"] == 0:
            itemsOrdered.append("Water")
        # Print out the errorstring if one exists and return None
        if errString != "":
            print(self.err(errString))
            return None
            
        else:
            return itemsOrdered

    # Truncates the order into the proper format by removing repeated entries
    # and putting the number of repeats next to the item
    # Input param: list orderNames: Array containing the name of every order (unformatted)
    # Returns an order in the proper format. Example would be:
    # ["Sandwich", "Chips", "Chips", "Soda"] ->
    # ["Sandwich", "Chips(2)", "Soda"]
    def __formatOrder(self, orderNames):
        # Create a hashMap so we can get the number of times per order 
        hashMap = {}
        # If the order does not exist in the hashMap, set its value equal 
        # to 1. If it does, increment the value by 1. 
        for i in range(len(orderNames)):
            item = orderNames[i]
            if orderNames[i] in hashMap:
                hashMap[item] += 1
            else: 
                hashMap[item] = 1
        # Insert the hashMap keys (the meal items) into a formatted array with the number of repeats
        formattedArray = []
        for key in hashMap:
            # If the item appears more than once, add to array with special formatting
            if hashMap[key] > 1:
                formattedArray.append(key + "(" + str(hashMap[key]) + ")")
            # Otherwise, don't change its formatting from normal 
            else:
                formattedArray.append(key)

        return formattedArray


    # Function that allows user to input a meal and receive the checked, validated
    # order in the form of a string.
    # Input params: String meal: meal selected by the user 
    #               List order: List of item IDs selected by the user for their order 
    # Output: Returns a string if the order has been validated, with the formatted, validated order 
    #         Returns None is the order is invalid
    def orderMeal(self, meal, order):
        # Check meal validity by comparing to values in menu
        if meal not in self._menu:
            return self.err(meal + " does not exist")
        
        # Create a dictionary with two list entries. 
        # 1) Orders: List of every order made (name of item)
        # 2) Types: List of every type included in the meal (name of type, like "Main", "Side", etc.)
        # The purpose is to be able to compare the meal names and their types later. 
        ordersWithTypes = {}
        itemNames = []
        itemTypes = []
        for num in order:
            # To line up with the indices of the menu and itemTypes dict + list, we subtract 
            # 1 from the number selected from the list of itemIDs in the order 
            num = int(num) - 1
            # If the item number is too low or too high, then we just have an error 
            if (num < 0 or num > 3 or (num > 2 and meal != "Dinner")):
                return self.err("Item ID does not exist")
            # Otherwise, append the name and its type to the same index of the two different lists
            itemNames.append(self._menu[meal][num])
            itemTypes.append(self._itemTypes[num])
        # Create the overall dictionary with the two corresponding lists
        ordersWithTypes["Orders"] = itemNames 
        ordersWithTypes["Types"] = itemTypes 
        
        # Validate the order by checking if it meets any error conditions.
        # If it doesn't, this function will also add necessary things (like water if no drink is ordered)
        validOrder = self.__checkOrder(meal, ordersWithTypes)
        # Handle error: is validOrder is none, the order is invalid, so we return None
        if validOrder == None:
            return None
        #If the order is valid, we format the order to display the amount of repeats next to each food item
        output = self.__formatOrder(validOrder)
        # Finally, we return the order in the form of a string for the main method to print
        return ', '.join(output)

    # Returns an error message for printing based on incorrect inputs 
    def err(self, error, item=None):
        errMessage = "Unable to process: "
        errMessage += error
        return errMessage


    