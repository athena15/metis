# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

SELECT * FROM Customers
WHERE Country='UK';

2. What is the name of the customer who has the most orders?

SELECT CustomerName, Count(OrderID) as count FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerId
GROUP BY CustomerName
ORDER BY count DESC

3. Which supplier has the highest average product price?

SELECT SupplierName, AVG(Price)
FROM Suppliers
JOIN Products ON Suppliers.SupplierID = Products.SupplierID;

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

SELECT DISTINCT COUNT(Country)
FROM Customers

5. What category appears in the most orders?

6. What was the total cost for each order?
SELECT OrderID, SUM(Price*Quantity) TotalCost
FROM OrderDetails JOIN Products
USING (ProductID)
GROUP BY OrderID
ORDER BY TotalCost DESC

7. Which employee made the most sales (by total price)?

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
