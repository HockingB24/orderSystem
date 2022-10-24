import unittest 
import sys
sys.path.append('../')
from src.orderSystem import OrderSystem

class TestOrder(unittest.TestCase):
    
    
    def test_check_order(self):
        """
        Test for the "check order" private function. If the order is invalid, this 
        method prints an error string and returns "None". If the order is valid, it returns the 
        array of the valid order (unformatted). (In the flow of the program, the order
        goes from the output of this function into format_order)
        Specific things it will say are errors:
            - Multiple main courses at any meal
            - Multiple side dishes at breakfast and dinner
            - No dessert chosen at dinner 
            - Either a main or a side is missing
        Other rules:
            - Adds water to every dinner, and every other meal missing a drink
        """
        # This order should be accepted.
        breakfast = "Breakfast"
        bPass = {
                    "Orders": ["Eggs", "Toast", "Coffee"],
                    "Types":  ["Main", "Side",  "Drink"]
                 }
        # This order fails because it has multiple side dishes. 
        bFail = {
                    "Orders": ["Eggs", "Toast", "Toast", "Coffee"],
                    "Types":  ["Main", "Side", "Side",  "Drink"]
                 }

        lunch = "Lunch"
        # This order passes. 
        lPass = {
                    "Orders": ["Sandwich", "Chips", "Soda"],
                    "Types":  ["Main", "Side",  "Drink"]
                }
        # This order fails because it has multiple main dishes. 
        lFail = {
                    "Orders": ["Sandwich", "Sandwich", "Chips", "Soda"],
                    "Types":  ["Main", "Main", "Side",  "Drink"]
                }
        
        dinner = "Dinner"
        # This order passes. Water should be added to the array of items.
        dPass = {
                    "Orders": ["Steak", "Potatoes", "Wine", "Cake"],
                    "Types":  ["Main", "Side",  "Drink", "Dessert"]
                }
        # This order fails because dessert is missing from dinner. 
        dFail = {
                    "Orders": ["Steak", "Chips", "Wine"],
                    "Types":  ["Main", "Side", "Drink"]
                }
        
        dPass = {
            "Orders": ["Steak", "Potatoes", "Wine", "Cake"],
            "Types":  ["Main", "Side",  "Drink", "Dessert"]
        }
        # This order fails because the main dish is missing.
        dFail2 = {
                    "Orders": ["Chips", "Wine", "Cake"],
                    "Types":  ["Side", "Drink", "Dessert"]
                }
        # This order fails because the side dish is missing.
        dFail3 = {
                    "Orders": ["Steak", "Wine", "Cake"],
                    "Types":  ["Main", "Drink", "Dessert"]
                }
                
        # Create the object for the test calls 
        system = OrderSystem()

        # Run all breakfast cases
        expectedbPass = ["Eggs", "Toast", "Coffee"]
        actualbPass = system._OrderSystem__checkOrder(breakfast, bPass)
        actualbFail = system._OrderSystem__checkOrder(breakfast, bFail)

        # Run all lunch cases
        expectedlPass = ["Sandwich", "Chips", "Soda"]
        actuallPass = system._OrderSystem__checkOrder(lunch, lPass)
        actuallFail = system._OrderSystem__checkOrder(lunch, lFail)

        # Run all dinner cases
        expecteddPass = ["Steak", "Potatoes", "Wine", "Water", "Cake"]
        actualdPass = system._OrderSystem__checkOrder(dinner, dPass)
        actualdFail = system._OrderSystem__checkOrder(dinner, dFail)
        actualdFail2 = system._OrderSystem__checkOrder(dinner, dFail2)
        actualdFail3 = system._OrderSystem__checkOrder(dinner, dFail3)

        # See if the cases match up with predictions (Failures are "None")
        self.assertEqual(actualbPass, expectedbPass)
        self.assertEqual(actualbFail, None)
        self.assertEqual(actuallPass, expectedlPass)
        self.assertEqual(actuallFail, None)
        self.assertEqual(actualdPass, expecteddPass)
        self.assertEqual(actualdFail, None)
        self.assertEqual(actualdFail2, None)
        self.assertEqual(actualdFail3, None)       


    def test_format_order(self):
        """
        Test that order is properly formatted.
        Specifically, the number of times each valid item appears should be 
        totalled next to the item in the array instead of the item being listed
        multiple times. 
        """

        # Create three orders containing multiple items
        order1 = ["Sandwich", "Chips", "Chips", "Soda"]
        order2 = ["Sandwich", "Chips", "Chips", "Chips", "Chips", "Soda"]
        order3 = ["Eggs", "Toast", "Coffee", "Coffee", "Coffee"]

        # Show the expected formatting 
        expected1 = ["Sandwich", "Chips(2)", "Soda"]
        expected2 = ["Sandwich", "Chips(4)", "Soda"]
        expected3 = ["Eggs", "Toast", "Coffee(3)"]

        system = OrderSystem()

        # Retrieve the actual results from the function 
        actual1= system._OrderSystem__formatOrder(order1)
        actual2 = system._OrderSystem__formatOrder(order2)
        actual3 = system._OrderSystem__formatOrder(order3)
        
        # Test if they match the proper values 
        self.assertEqual(actual1, expected1)
        self.assertEqual(actual2, expected2)
        self.assertEqual(actual3, expected3)
    

    

if __name__ == '__main__':
    unittest.main()
