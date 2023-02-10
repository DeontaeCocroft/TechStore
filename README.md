# TechStore Database Python Program
My code is a python program that reads, writes, and deletes information to and from my PostgreSQL database. There is a password for authentication and there are administrarive prviligaes. My program contains 9 functions exfluding main(). Here is an explanation of my functions.

ciview() which connects to the database, executes a sql statement, and prints the customer information from the database. Once this takes if my admin counter equals 1 then the adminmenu() function will be called after this fuction is done. If my admin couter is 0 the the menu() function will be called.

psiview() which connects to the database, executes a sql statement, and prints products and supplier information from the database.Once this takes if my admin counter equals 1 then the adminmenu() function will be called after this fuction is done. If my admin couter is 0 the the menu() function will be called.

opciview() which connects to the databse, executes a sql statement, and prints orders with product and customer information from the database.Once this takes if my admin counter equals 1 then the adminmenu() function will be called after this fuction is done. If my admin couter is 0 the the menu() function will be called.

addcustomer() which allows the user to add a new customer to the database. The current customers will be shown and the user will be presented with inputs to add the new customers information in. Once this information is entered the values are put into an sql statement that adds the customer. After the customer is added the ciview() function will be called to display the customer and the new customer will be found there. Once this takes if my admin counter equals 1 then the adminmenu() function will be called after this fuction is done. If my admin couter is 0 the the menu() function will be called.

delcustomer() which allows the user to delete a customer from the database. The current customers will be shown and the user will be presented with an input to enter the customers ID that corresponds to the customer they want to delete. After the customer is deleted the ciview() function is called to display the customers and you will see the customer is no longer present.

login() which allows the user to select the admin login or regular login. Upon selecting a login option the user has to enter in the correct username and passwod for that specific login option. If the username or password is incorrect the user will be notified and promped to try again. This will happen until the username and password is correct. If the user has the correct cresidentials for the admin login the will be granted access to the adminmenu which has additional options. Admin access will also trigger a counter which keeps track of things going in and out the menu options. This is to ensure that non admin users DO NOT get admin access. Non admin users will be granted access to a menu which is a limited version of the adminmenu.

exitprogram() which simpily closses the program and prints the user a goodbye message

def menu() which is the non administrator menu and allows the user to access the functions ciview(), psiview(), opciview(), login(), and exitprogram(). These 5 functions are called using the numbers 1-5 and if the user enters a value other than the menu options they will be propted to try again and given another chance until they select a correct option.

def adminmenu() which is the administrator menu allows the user to access the functions ciview(), psiview(), opciview(), addcustomer(), delcustomer(), login(), and exitprogram(). These 7 functions are called using the numbers 1-7 and if the user enters a value other than the menu options they will be propted to try again and given another chance until they select a correct option. Since this is the admin menu the user will be promted that they are in the admin menu. 

