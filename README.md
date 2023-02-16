# TechStore Database Python Program Explanation

My code is a python program that reads, writes, and deletes information to and from my PostgreSQL database. There is a password for authentication and there are administrative privileges. My program contains 9 functions excluding main(). Here is an explanation of my functions.

ciview() which connects to the database, executes a SQL statement, and prints the customer information from the database. Once this takes place, if my admin counter equals 1 then the adminmenu() function will be called after this function is done. If my admin counter is 0 then the menu() function will be called.

psiview() which connects to the database, executes a SQL statement, and prints products and supplier information from the database. Once this takes place, if my admin counter equals 1 then the adminmenu() function will be called after this function is done. If my admin counter is 0 then the menu() function will be called.

opciview() which connects to the database, executes a SQL statement, and prints orders with product and customer information from the database. Once this takes place, if my admin counter equals 1 then the adminmenu() function will be called after this function is done. If my admin counter is 0 then the menu() function will be called.

addcustomer() which allows the user to add a new customer to the database. The current customers will be shown, and the user will be presented with inputs to add the new customers information in. Once this information is entered, the values are put into a SQL statement that adds the customer. After the customer is added, the ciview() function will be called to display the customer and the new customer will be found there. Once this takes place, if my admin counter equals 1 then the adminmenu() function will be called after this function is done. If my admin counter is 0 then the menu() function will be called.

delcustomer() which allows the user to delete a customer from the database. The current customers will be shown, and the user will be presented with an input to enter the customer's ID that corresponds to the customer they want to delete. After the customer is deleted, the ciview() function is called to display the customers and you will see the customer is no longer present.

login() which allows the user to select the admin login or regular login. Upon selecting a login option, the user has to enter the correct username and password for that specific login option. If the username or password is incorrect, the user will be notified and prompted to try again. This will happen until the username and password is correct. If the user has the correct credentials for the admin login, they will be granted access to the adminmenu which has additional options. Admin access will also trigger a counter which keeps track of things going in and out of the menu options. This is to ensure that non admin users DO NOT get admin access. Non admin users will be granted access to a menu which is a limited version of the adminmenu.

exitprogram() which simply closes the program and prints the user a goodbye message

def menu() which is the non administrator menu and allows the user to access the functions ciview(), psiview(), opciview(), login(), and exitprogram(). These 5 functions are called using the numbers 1-5 and if the user enters a value other than the menu options they will be prompted to try again and given another chance until they select the correct option.

def adminmenu() which is the administrator menu allows the user to access the functions ciview(), psiview(), opciview(), addcustomer(), delcustomer(), login(), and exitprogram(). These 7 functions are called using the numbers 1-7 and if the user enters a value other than the menu options they will be prompted to try again and given another chance until they select the correct option. Since this is the admin menu, the user will be notified that they are in the admin menu. 

When completing this project, I made sure to handle all possible errors that I can think of and keep the program running until the user decides to close the program. Even if the user messes up along the way and types in incorrect information, the program will notify them and redirect to keep things flowing.
