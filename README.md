Panache Food Ordering App
Project Title

Panache Food Ordering Console Application in Python

Overview of the Project

Panache Food Ordering Application is a simple console Python application, through which people can view the menu, select food items, and get a final bill of the ordered food.
It uses core Python concepts like dictionaries, loops, input handling, functions, and modular code structuring.

It displays a menu, asks multiple orders from the people, processes the input, calculates the total price of items, and prints a formatted final bill.
This project will be ideally suited for beginners learning Python basics or as a mini-project work.

Features

 Menu Display

It displays all the available food items with their prices.

 Order Selection

It will continue to prompt the user to select menu items until the user types "done".

 Input Validation

Prevents invalid entries for the wrong item number or non-numeric values.

 Bill Generation

Prints a neat final bill with individual items and prices.

	Total Calculation

Automatically sums up the total order amount.

 Modular Code

Functions are maintainable and can be extended with ease.

Technologies / Tools Used

• Python 3.x

• Python's built-in modules only, no external libraries.

• Console / Terminal to execute the code.

Steps to Install & Run the Project

1. Install Python

Install Python 3.x if it's not installed:
python -- Version

2. Download or Copy the Project File

Save your Python code into a file named:

panache_food_order.py

3. Open a Terminal / Command Prompt
Navigate to the folder where the file is saved:
cd path/to/your/project

4. Run the Application
python panache_food_order.py
A console that launches the food ordering system Panache

Instructions for Testing

Try testing the program with the following scenarios to make sure it works as it should:

1. View Menu
Confirm that all 8 items appear, with correct names and prices.

2. Valid Order Input
Please enter valid item numbers such as 1, 3, 5.

3. Handling Invalid Input
Try entering:
Letters, e.g., "abc";

• Item numbers that are not on the menu; for example 20

• Special characters

The application must prompt the user to try again.


 4. Multiple Items Order several items and ensure the bill lists all of them.
  
 5.  Use “done” to finish ordering Type "done" to complete the selection and go directly to billing.
  
 6. Empty Order If the user types "done" immediately:
 
• The program should display "No items ordered."

