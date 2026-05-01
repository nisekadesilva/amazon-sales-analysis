--! Total Sales --!

SELECT SUM (total_sales) AS total_sales
FROM OrderItems;

--! Top Selling products --!
SELECT p.product_name, SUM(O.quantity) AS total_sold
FROM OrderItems O
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

--! Top Customers --!
SELECT c.customer_name,
    SUM(o.total_sales) AS total_spent
FROM Orders ord
JOIN Customers c ON ord.customer_id = c.customer_id
JOIN OrderItems o ON ord.order_id = o.order_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;

--! Sales by Category --!
SELECT  p.category,SUM(o.total_sales) AS revenue
FROM OrderItems o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;