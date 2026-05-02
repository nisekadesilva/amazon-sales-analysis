# E-Commerce Sales & Customer Behavior Analysis

## <ins> Project Overview </ins>
This project analyzes e-commerce sales data to understand customer behavior, product performance, and revenue trends.
The dataset was transformed from a flat structure into a relational database using SQL, and insights were visualized using Power BI dashboards.

##  <ins> Why This Project Important </ins>
In real-world e-commerce systems, data is not stored in a single table but in multiple related tables.
This project demonstrates how raw transactional data can be structured into a relational database and used to generate meaningful business insights.
It helps businesses understand customer purchasing patterns, top-performing products, and sales trends for better decision-making.

### <ins> Data Collection </ins>
I obtained an e-commerce sales dataset from Kaggle, which included order details such as product, category, price, customer information, and payment methods.

### <ins> Data Preparation </ins>

The dataset was originally in a flat format, where all information was stored in a single table.
This structure caused data duplication and was not suitable for efficient analysis.

###  <ins> Database Design </ins>

To solve this, I redesigned the dataset into a relational database using SQL.
The data was split into multiple tables:

- Customers
- Orders
- Products
- Order Items

This normalization process reduced redundancy and improved data organization.

### <ins> Data Processing </ins>

The raw dataset was imported into a SQLite database and transformed into structured tables using SQL queries.
Relationships were established using primary and foreign keys.

### <ins> Data Analysis </ins>

QL queries were used to analyze,

- Top-selling products
- Customer spending patterns
- Sales by category
- Payment method usage

### <ins> Visualization </ins>

The processed data was then connected to Power BI to create an interactive dashboard.
The dashboard provides clear insights into sales performance and customer behavior.


Page 1 | EXECUTIVE SALES OVERVIEW

The Executive Sales Overview dashboard provides a high-level summary of the e-commerce business performance.
The total sales reached 4 million across 250 orders and approximately 2,000 customers, indicating a moderate transaction volume with relatively high-value purchases.

💳 Payment Insights

Payment method analysis shows that PayPal (28.56%) and Credit Card (25.26%) are the most preferred options, indicating strong customer trust in digital payment systems.
In contrast, Debit Card usage (13.08%) is relatively low, suggesting an opportunity to promote alternative payment incentives.

🌍 Customer Distribution Insights

Customer distribution is concentrated in major cities such as Boston, Dallas, Houston, Miami, and New York, each contributing around 180 customers.
However, Los Angeles shows lower customer engagement (~120 customers), indicating a potential market expansion opportunity.

💰 Revenue by Location

Sales performance varies significantly by location.
Miami generates the highest revenue (507,200), making it the most valuable market, while San Francisco records the lowest (259,120), suggesting lower customer spending or demand.

📦 Product Category Insights

Among product categories, Electronics dominate total sales, highlighting strong demand for tech products.
In contrast, Books generate the lowest revenue, indicating weaker performance and possible need for promotional strategies.
