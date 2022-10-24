import unittest 
import sys
sys.path.append('../')

from src.orderSystem import OrderSystem

class TestOrder(unittest.TestCase):

    def test_dinner_no_dessert(self):
        """
        Test to ensure that improper dinner order returns an error
        """
        # Set meal and order, and use orderMeal function 
        meal = "Dinner"
        order = ["1","2","3"]
        system = OrderSystem()
        myOrder = system.orderMeal(meal, order)
        # Should return no order since it is invalid
        self.assertEqual(myOrder, None)
    
    def test_meal_without_drink(self):
        """
        Test to ensure water is added when necessary. 
        It should be added to all dinner orders, and any order not containing a drink (itemID: 3)
        """
        dinOrder   = ["1", "2", "3", "4"] # Main, Side, Wine, Dessert
        lunchOrder = ["1", "2"] # Main, Side
        breakOrder = ["1", "2"] # Main, Side
        system = OrderSystem()
        dinner = system.orderMeal("Dinner", dinOrder)
        lunch = system.orderMeal("Lunch", lunchOrder)
        breakfast = system.orderMeal("Breakfast", breakOrder)

        # Should return the proper order with Water included at the correct place.
        # For dinner, this is the second spot from the end, and for everything 
        # else, it's the last spot.
        self.assertEqual(dinner, "Steak, Potatoes, Wine, Water, Cake")
        self.assertEqual(lunch, "Sandwich, Chips, Water")
        self.assertEqual(breakfast, "Eggs, Toast, Water")
    
    def test_multiple_orders_accepted(self):
        """
        Test to make sure that multiple sides at lunch and 
        multiple drinks at breakfast are accepted
        """
        # Lunch accepts multiple sides, Breakfast accepts multiple drinks
        lunchOrder = ["1", "2", "2", "3"] # Main, Side
        breakOrder = ["1", "2", "3", "3"] # Main, Side

        system = OrderSystem()
        lunch = system.orderMeal("Lunch", lunchOrder)
        breakfast = system.orderMeal("Breakfast", breakOrder)

        # The returned string should be equal to the below output
        # with the number of items ordered next to the item
        self.assertEqual(lunch, "Sandwich, Chips(2), Soda")
        self.assertEqual(breakfast, "Eggs, Toast, Coffee(2)")
    

    def test_multiple_orders_failed(self):
        """
        Test to make sure that multiple main dishes,
        multiple sides (not at lunch), and multiple drinks
        (not at breakfast) throw errors, returning "None".
        """
        # We cannot have multiple mains, multiple sides (not at lunch),
        # or multiple drinks (not at breakfast)
        multipleMains = ["1", "1", "2", "3"] # Main, Main, Side, Drink
        multipleSides = ["1", "2", "2", "3"] # Main, Side, Side, Drink 
        multipleDrinks = ["1", "2", "3", "3"] # Main, Side, Drink, Drink 
        system = OrderSystem()
        multipleMainsActual = system.orderMeal("Breakfast", multipleMains)
        multipleSidesActual = system.orderMeal("Dinner", multipleSides)
        multipleDrinksActual = system.orderMeal("Lunch", multipleDrinks)

        # All inputs here should return proper errors (return None and print error string)
        self.assertEqual(multipleMainsActual, None)
        self.assertEqual(multipleSidesActual, None)
        self.assertEqual(multipleDrinksActual, None)

    

if __name__ == '__main__':
    unittest.main()
