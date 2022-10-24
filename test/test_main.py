import unittest 
import sys
sys.path.append('../')

from src.orderSystem import OrderSystem

class TestOrder(unittest.TestCase):

    def test_dinner_no_dessert(self):
        """
        Test to ensure that improper dinner order returns an error
        """
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

        self.assertEqual(dinner, "Steak, Potatoes, Wine, Water, Cake")
        self.assertEqual(lunch, "Sandwich, Chips, Water")
        self.assertEqual(breakfast, "Eggs, Toast, Water")
    
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

        self.assertEqual(dinner, "Steak, Potatoes, Wine, Water, Cake")
        self.assertEqual(lunch, "Sandwich, Chips, Water")
        self.assertEqual(breakfast, "Eggs, Toast, Water")
    
    #def test_
    

if __name__ == '__main__':
    unittest.main()
