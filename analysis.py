import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('database/database.db')


#Product Analysis

# top products
querytop = """
SELECT p.product_name, SUM(oi.total_sales) AS sales
FROM Products p
JOIN OrderItems oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY sales DESC
LIMIT 10; 
"""

# load data
df = pd.read_sql(querytop, conn)

print(df)  # check data


# plot
df.plot(kind='bar', x='product_name', y='sales')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()

#Low-performing products
querylow = """SELECT p.product_name, SUM(oi.total_sales) AS sales
FROM Products p
JOIN OrderItems oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY sales ASC
LIMIT 10;"""

# load data    
df = pd.read_sql(querylow, conn)

print(df)  # check data

# plot
df.plot(kind='bar', x='product_name', y='sales')
plt.title("Low-performing Products")   
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


#Customer Analysis

# top customers
querytopcust = """SELECT c.customer_name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;"""

# load data
df = pd.read_sql(querytopcust, conn) 
print(df)  
# plot
df.plot(kind='bar', x='customer_name', y='total_spent')
plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Customer")
plt.ylabel("Total Spent")
plt.xticks(rotation=45)
plt.show()

# low-performing customers
querylowcust = """SELECT c.customer_name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_spent ASC
LIMIT 10;"""

# load data
df = pd.read_sql(querylowcust, conn)
print(df)
# plot
df.plot(kind='bar', x='customer_name', y='total_spent')
plt.title("Low-performing Customers")
plt.xlabel("Customer")
plt.ylabel("Total Spent")
plt.xticks(rotation=45)
plt.show()

#Number of orders per customer
queryorders = """SELECT c.customer_name, COUNT(o.order_id) AS order_count
FROM Customers c 
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY order_count DESC;"""

# load data
df = pd.read_sql(queryorders, conn)
print(df)
# plot
df.plot(kind='bar', x='customer_name', y='order_count')
plt.title("Number of Orders per Customer")
plt.xlabel("Customer")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.show()

#Average order value
queryaov = """SELECT c.customer_name, AVG(o.total_amount) AS average_order_value    
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY average_order_value DESC;"""

# load data
df = pd.read_sql(queryaov, conn)

print(df)
# plot
df.plot(kind='bar', x='customer_name', y='average_order_value')
plt.title("Average Order Value per Customer")
plt.xlabel("Customer")
plt.ylabel("Average Order Value")
plt.xticks(rotation=45)
plt.show()


#Category Analysis

querycat = """SELECT p.category, SUM(oi.total_sales) AS sales
FROM Products p
JOIN OrderItems oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY sales DESC;"""

# load data
df = pd.read_sql(querycat, conn)
print(df)
# plot
df.plot(kind='bar', x='category', y='sales')
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

#Top Product For Category
querytopcat = """SELECT p.category, p.product_name, SUM(oi.total_sales) AS sales
FROM Products p
JOIN OrderItems oi ON p.product_id = oi.product_id
GROUP BY p.category, p.product_name
ORDER BY p.category, sales DESC;"""

# load data
df = pd.read_sql(querytopcat, conn)
print(df)
# plot
for category in df['category'].unique():
    subset = df[df['category'] == category]
    plt.bar(subset['product_name'], subset['sales'])
    plt.title(f"Top Products in {category}")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()