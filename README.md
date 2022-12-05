# TechStoreDatabase
# TechStoreDatabase
|How it works|
The PythonDatabaseAccess file is my python code which connects to my TechStore Postgresql database using psycopg2.
I used Eclipse Python and Postgresql to create this connection.
To start This program has a password that needs to be entered.
If the password is entered incorrectly the user will be prompted "Wrong Password, Please try again! and will have to enter the correct password.
Once the user enters the correct password they will be granted access and greeted with options to display specific queries of information from the database.
Option '1' Displays the customers from the database.
Option '2" Displays Product and supplier information from the database.
Option '3' Displays Orders with customer, product, and order information from the database.
Option '4' Closes the program and gives the user a Goodbye message.
If an option is entered that is not listed the user will be prompted to try again and select an appropriate option.

This program contains 6 functions:

1.) “def key():” is a function that protects this application from unwanted users. 
This function takes user input as a password.
This was done by using a user scanner aka “input” in python.
If that password is not correct they will be prompted to try again and will not gain access into the program unless the correct password is entered.
This was done by creating a while loop.
If the password is correct then the program will move to the ‘def options():’ function.
This was done by using a if then statement.

2.) “def options();”  is a function that takes user input and allows them to select a specific option using a user scanner aka “input” in python.
Option “1” calls “def ciview()”.
Option “2” calls “def psiview()”.
Option “3” calls “def opciview()”.
Option “4” calls “def exitprogram()”.

This was done by using if and elif statements.
If the user enters a value that does not equal one of these options they will be prompted to enter the correct option and they will be prompted the options again. 
This was done by creating a while loop .

3.) “def ciview():” is a function that connects to the Postgresql database and displays customer information from that database. 
This function is called by selecting Option “1”.
This is done by using psycopg2 to create a connection and creating a cursor to execute statements to communicate with the MySQL database.
Then the cursor is executed with an sql statement that pulls information from tables in the Postgresql database.
After the cursor is executed a record is created to fetch the data from the sql statement and that record is printed to in the function.
After the customer information is displayed the cursor and connection is closed and the options() function is called to display the options again.

4.) “def psiview():'' is a function that connects to the Postgresql database and displays Products and supplier information from that database. 
This function is called by selecting Option “2”.
This is done by using psycopg2 to create a connection and creating a cursor to execute statements to communicate with the MySQL database.
Then the cursor is executed with an sql statement that pulls information from tables in the Postgresql database.
After the cursor is executed a record is created to fetch the data from the sql statement and that record is printed to in the function.
After the Products and supplier information is displayed the cursor and connection is closed and the options() function is called to display the options again.


5.) “def opciview():” is a function that connects to the Postgresql database and displays customer information from that database. 
This function is called by selecting Option “3”.
This is done by using psycopg2 to create a connection and creating a cursor to execute statements to communicate with the MySQL database.
Then the cursor is executed with an sql statement that pulls information from tables in the Postgresql database.
After the cursor is executed a record is created to fetch the data from the sql statement and that record is printed to in the function.
After the Products and supplier information is displayed the cursor and connection is closed and the options() function is called to display the options again.

6.) “def exitprogram():” is a function that simply closes the program and prints a goodbye message.
This function is called by selecting Option “4”.


