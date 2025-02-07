-- inserts in many row in the table customer (database alx_book_store) as data given in MySQL server.
USE alx_book_store;
SELECT * FROM Customers;
INSERT INTO customers(customer_id, customer_name, email,address)
VALUES("2","Blessing Malik", "bmalik@sandtech.com", "124 Happiness  Ave."),("3","Obed Ehoneah", "eobed@sandtech.com" , "125 Happiness  Ave."), ("4","Nehemial Kamolu", "nkamolu@santech.com", "126 Happiness  Ave.");
