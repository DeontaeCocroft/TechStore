--Deontae M Cocroft TechStore Database 4 December 2022

--TechStore Table Creation

CREATE TABLE SUPPLIER_CONTACT_INFO(
	ContactID SERIAL not null,
	ContactTitle varchar(255) not null,
	ContactFirstName varchar(255) not null,
	ContactLastName varchar(255) not null,
	ContactEmail varchar(255) not null,
	CONSTRAINT ContactIDPK PRIMARY KEY (ContactID)
);

CREATE TABLE SUPPLIER_INFO(
	CompanyName varchar(255) not null,
	Address varchar(255) not null,
	PostalCode int not null,
	City varchar(255) not null,
	State varchar(255) not null,
	Country varchar(255) not null,
	Phone bigint not null,
	Fax bigint not null,
	Website varchar(255),
	CONSTRAINT CompanyNamePK PRIMARY KEY (CompanyName)
);

CREATE TABLE SUPPLIERS(
	SupplierID SERIAL not null,
	ContactID int not null,
	CompanyName varchar(255) not null,
	CONSTRAINT SupplierIDPK PRIMARY KEY (SupplierID),
	CONSTRAINT ContactIDFK FOREIGN KEY (ContactID) REFERENCES SUPPLIER_CONTACT_INFO(ContactID),
	CONSTRAINT CompanyNameFK FOREIGN KEY (CompanyName) REFERENCES SUPPLIER_INFO(CompanyName)
);

CREATE TABLE CATEGORY(
	CategoryID SERIAL not null,
	CategoryName varchar(255) not null,
	Description varchar(255) not null,
	CONSTRAINT CategoryIDPK PRIMARY KEY (CategoryID)
);

CREATE TABLE PRODUCTS(
	ProductID SERIAL not null,
	SupplierID int not null,
	CategoryID int not null,
	ProductName varchar(255) not null,
	MSRP money not null,
	Color varchar(255),
	Style varchar(255),
	Manufacturer varchar(255) not null,
	QuantityOnHand int not null,
	UnitsOrdered int not null,
	Description varchar(255),
	CONSTRAINT ProductIDPK PRIMARY KEY (ProductID),
	CONSTRAINT SupplierIDFK FOREIGN KEY (SupplierID) REFERENCES SUPPLIERS(SupplierID),
	CONSTRAINT CategoryIDFK FOREIGN KEY (CategoryID) REFERENCES CATEGORY(CategoryID)
);

CREATE TABLE CUSTOMERS(
	CustomerID SERIAL not null,
	FirstName varchar(255) not null,
	LastName varchar(255) not null,
	Address varchar(255) not null,
	PostalCode int not null,
	City varchar(255) not null,
	State varchar(255) not null,
	Country varchar(255) not null,
	Email varchar(255) not null,
	PhoneNumber bigint not null,
	CONSTRAINT CustomerIDPK PRIMARY KEY (CustomerID)
);

CREATE TABLE ORDER_INFO(
	OrderInfoID SERIAL not null,
	ProductID int not null,
	Quantity int not null,
	Price money not null,
	SalesTax money not null,
	Total money not null,
	CONSTRAINT OrderInfoIDPK PRIMARY KEY (OrderInfoID),
	CONSTRAINT ProductIDFK FOREIGN KEY (ProductID) REFERENCES PRODUCTS(ProductID)
);

CREATE TABLE ORDERS(
	OrderID SERIAL not null,
	OrderInfoID int not null,
	CustomerID int not null,
	OrderDate date not null,
	CONSTRAINT OrderIDPK PRIMARY KEY (OrderID),
	CONSTRAINT CustomerIDFK FOREIGN KEY (CustomerID) REFERENCES CUSTOMERS(CustomerID),
	CONSTRAINT OrderInfoIDFK FOREIGN KEY (OrderInfoID) REFERENCES ORDER_INFO(OrderInfoID)
);



--SUPPLIER_CONTACT_ INFO Table Inserts

INSERT INTO SUPPLIER_CONTACT_INFO (ContactTitle, ContactFirstName, ContactLastName, ContactEmail)
VALUES 
('OWNER', 'Glen', 'Page', 'HEHGlenpage@outlook.com'),
('OWNER', 'Jay', 'Russel','Jayr@outlook.com');

--SUPPLIER_INFO Table Inserts

INSERT INTO SUPPLIER_INFO (CompanyName, Address, PostalCode, City, State, Country, Phone, Fax, Website)
VALUES 
('High End Hardware INC','8028 Monroe Street','33308', 'Fort Lauderdale', 'Florida','United States', '2075506915', '3059206491', ''),
('GPU Hardware LLC','6 Grand Ave', '11368', 'Corona', 'New York','United Stats', '5059490766', '6461287347', 'www.JaysGPUHardware.com');

--SUPPLIERS Table Inserts

INSERT INTO SUPPLIERS (ContactID, CompanyName)
VALUES 
('7', 'High End Hardware INC'),
('8', 'GPU Hardware LLC');

--CATEGORY Table Inserts

INSERT INTO CATEGORY (CategoryName, Description)
VALUES 
('GPU', 'Graphical Processing Units From GPU Hardware LLC'),
('CPU', 'Central Processing Units From High End Hardware INC');

--PRODUCTS Table Inserts

INSERT INTO PRODUCTS (SupplierID, CategoryID, ProductName, MSRP, Color, Style, Manufacturer, QuantityOnHand, UnitsOrdered, Description)
VALUES 
('4', '1', 'GTX 1650', '149', 'Black & Grey', 'Phoenix', 'ASUS', '100', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1650', '149', 'Black & Grey', 'SC Ultra Gaming', 'EVGA', '110', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1650 Super', '160', 'Black & Grey', 'SC Ultra Gaming', 'EVGA', '100', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1650 Super', '160', 'Black & Grey', 'SC Ultra Gaming', 'EVGA', '100', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1650 Super', '160', 'Black & Grey', 'SC Ultra Gaming', 'EVGA', '100', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1660', '219', 'Black', '', 'Zotac Gaming', '200', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1660', '219', 'Black & Grey', 'SC Ultra Gaming', 'EVGA', '120', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1660 Super', '229', 'Black & Light Grey', 'Ventus XS', 'MSI', '120', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1660 Super', '229', 'Black & Light Grey', 'Gaming X', 'MSI', '170', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'GTX 1660 Ti', '279', 'Black', 'OC', 'GIGABYTE', '170', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2060', '349', 'Black & Light Grey', 'KO Ultra Gaming', 'EVGA', '170', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2060 Super', '349', 'Black & Light Grey', 'KO Ultra Gaming', 'EVGA', '170', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2070', '449', 'Black', 'XC Ultra Gaming', 'EVGA', '90', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2070 Super', '499', 'Black & Light Grey', 'Founders Edition', 'NVIDIA', '20', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2080', '699', 'Black', 'OC Edition', 'ASUS', '50', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2080 Super', '699', 'Black', 'Gaming X Trio', 'MSI', '42', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2080 Ti', '999', 'Black', 'RTW3 Ultra', 'MSI', '26', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 2080 Ti', '999', 'Black', 'ROG Strix', 'ASUS', '20', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3060', '329', 'Black', 'Gaming X', 'MSI', '350', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3060', '329', 'Black & Dark Grey', 'Twin Edge OC', 'ZOTAC Gaming', '400', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3060 TI', '399', 'Black', 'Gaming X', 'MSI', '250', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3070', '499', 'Black', 'Gaming Z Trio', 'MSI', '190', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3070', '499', 'Black', 'Gaming OC', 'GIGABYTE', '150', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3070 Ti', '599', 'Black', 'AMP Holo', 'ZOTAC Gaming', '120', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3080', '699', 'White', 'Trinity OC White Edition', 'ZOTAC Gaming', '100', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3080 TI', '1119', 'Black & Dark Grey', 'XC3 Ultra Gaming', 'EVGA', '30', '0','GPU FROM GPU Hardware LLC'),
('4', '1', 'RTX 3090', '1499', 'Black & Dark Grey', 'FTW3 Ultra Gaming', 'EVGA', '9', '0','GPU FROM GPU Hardware LLC');


--CUSTOMER Table Inserts

INSERT INTO CUSTOMERS(FirstName, LastName, Address, PostalCode, City, State, Country, Email, PhoneNumber)
VALUES 
('Deontae', 'Cocroft', '20015 S LaGrange Road', '60423', 'Frankfort', 'Illinois', 'United States', 'dcocroft815@gmail.com', '7085060000'),
('Eunice', 'Johnston', '7007 Hawthorne St', '20782', 'Hyattsville', 'Maryland', 'United States', 'Eujohn261@outlook.com', '2002918213'),
('Clark', 'Mcdaniel', '848 Oklahoma Lane', '93306', 'Bakersfield', 'California', 'United States', 'ClackMD01@gmail.com', '3198761224'),
('Nellie', 'Higgins', '920 Plymouth Court', '49428', 'Jenison', 'Michigan', 'United States', 'NH2671@comcast.net', '2195267020'),
('Krista', 'Strickland', '107 San Pablo Street', '75088', 'Rowlett', 'Texas', 'United States', 'Krists&@gmail.com', '5056647135'),
('Helen', 'Turner', '9785 Coffee St', '46804', 'Fort Wayne', 'Indiana', 'United States', 'Helen1234@gmail.com', '2012587021'),
('Doyle', 'Boone', '211 Ohio Drive', '11552', 'West Hempstead', 'New York', 'United States', 'BooneD@gmail.com', '2053623771'),
('Shawna', 'Marsh', '91 Green Hill St', '92111', 'San Diego', 'California', 'United States', 'ShawnaM1995@gmail.com', '3252385683');

--ORDER_INFO Table Inserts & PRODUCTS Table Updates

INSERT INTO ORDER_INFO (ProductID, Quantity, Price, SalesTax, Total)
VALUES ('20','2','329','41.125','699.125');

UPDATE PRODUCTS
SET UnitsOrdered = 2
WHERE ProductID = 20;

INSERT INTO ORDER_INFO (ProductID, Quantity, Price, SalesTax, Total)
VALUES ('27','1','1499','93.6875','1592.6875');

UPDATE PRODUCTS
SET UnitsOrdered = 1
WHERE ProductID = 27;

INSERT INTO ORDER_INFO (ProductID, Quantity, Price, SalesTax, Total)
VALUES ('1','5','149','46.5625','791.5625');

UPDATE PRODUCTS
SET UnitsOrdered = 5
WHERE ProductID = 1;

INSERT INTO ORDER_INFO (ProductID, Quantity, Price, SalesTax, Total)
VALUES ('19','1','329','20.5625','349.5625');

UPDATE PRODUCTS
SET UnitsOrdered = 1
WHERE ProductID = 19;

--ORDERS Table Inserts

INSERT INTO ORDERS(OrderInfoID, CustomerID, OrderDate)
VALUES 
('1', '1', '12/4/2022'),
('2', '2', '12/4/2022'),
('3', '5', '12/4/2022'),
('4', '8', '12/4/2022');



