# Menu Ordering System Challenge

Hello!

I created this menu ordering system in Python 3.9.6. There should be no dependencies to install, but the program does import the unit testing framework called 'unittest', and the module called 'sys'. 'Sys' is used to retrieve command-line arguments for the program, and 'unittest' was used to do unit testing on the OrderSystem class.

--------------------

## Build and Run

### Main file

There are no build scripts -- to run the main file, just navigate to the root of the directory that contains main.py and run the command:

 `python3 main.py inputargs`

Here are two examples using the input arguments from the design document:

`python3 main.py Breakfast 1,2,3,3,3`

`python3 main.py Lunch 1,2,3`

### Test files

To run the tests, navigate to the test folder and run:

`python3 test_functions.py`

`python3 test_main.py`

test_functions.py tests the private functions of the OrderSystem class to ensure they give the correct output in support of the main, orderMeal() function. test_main.py tests the orderSystem.orderMeal() function, which is the only public function that is used in the main method to validate and return the order.

