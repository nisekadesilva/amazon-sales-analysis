INSERT INTO Customers (customer_location , customer_name)
SELECT DISTINCT "customer location" , "customer name"
FROM raw_data;

INSERT INTO Products (product_name , category , price)
SELECT DISTINCT "product" , "category" , "price"   
FROM raw_data;

INSERT INTO Orders (order_id, order_date, customer_id, payment_method)
SELECT
    r."Order ID",
    r."Date",
    c.customer_id,
    r."Payment Method"
FROM raw_data r
JOIN Customers c
ON r."Customer Name" = c.customer_name
AND r."Customer Location" = c.customer_location
GROUP BY r."Order ID";


INSERT INTO OrderItems (order_id, product_id, quantity, total_sales)
SELECT
    r."Order ID",
    p.product_id,
    r."Quantity",
    r."Total Sales"
FROM raw_data r
JOIN Products p
ON r."Product" = p.product_name
AND r."Category" = p.category
AND r."Price" = p.price;

