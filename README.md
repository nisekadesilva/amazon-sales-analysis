# E-Commerce Sales & Customer Behavior Analysis

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black&style=flat-square)
![DAX](https://img.shields.io/badge/DAX-F97316?logo=microsoft&logoColor=white&style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white&style=flat-square)
![Python](https://img.shields.io/badge/Python-F97316?logo=python&logoColor=white&style=flat-square)

## <img src="https://cdn.simpleicons.org/target/14B8A6" width="20"/> | <ins> Project Overview </ins>
This project analyzes e-commerce sales data to understand customer behavior, product performance, and revenue trends.
The dataset was transformed from a flat structure into a relational database using SQL, and insights were visualized using Power BI dashboards.

##  <ins> Why This Project Important </ins>
In real-world e-commerce systems, data is not stored in a single table but in multiple related tables.
This project demonstrates how raw transactional data can be structured into a relational database and used to generate meaningful business insights.
It helps businesses understand customer purchasing patterns, top-performing products, and sales trends for better decision-making.

### <img src="https://cdn.simpleicons.org/databricks/14B8A6" width="20"/> | <ins> Data Collection </ins>
I obtained an e-commerce sales dataset from Kaggle, which included order details such as product, category, price, customer information, and payment methods.

### <ins> Data Preparation </ins>

The dataset was originally in a flat format, where all information was stored in a single table.
This structure caused data duplication and was not suitable for efficient analysis.

### <img src="https://cdn.simpleicons.org/sqlite/14B8A6" width="20"/> | <ins> Database Design </ins>

To solve this, I redesigned the dataset into a relational database using SQL.
The data was split into multiple tables:

- Customers
- Orders
- Products
- Order Items

This normalization process reduced redundancy and improved data organization.

### <img src="https://cdn.simpleicons.org/pandas/14B8A6" width="20"/> | <ins> Data Processing </ins>

The raw dataset was imported into a SQLite database and transformed into structured tables using SQL queries.
Relationships were established using primary and foreign keys.

### <img src="https://cdn.simpleicons.org/googleanalytics/14B8A6" width="20"/>  | <ins> Data Analysis </ins>

QL queries were used to analyze,

- Top-selling products
- Customer spending patterns
- Sales by category
- Payment method usage

### <img src="https://cdn.simpleicons.org/powerbi/14B8A6" width="20"/>  | <ins> Visualization </ins>

The processed data was then connected to Power BI to create an interactive dashboard.
The dashboard provides clear insights into sales performance and customer behavior.

----

### <ins> Page 1 | EXECUTIVE SALES OVERVIEW </ins>
<br>
<img width="1324" height="780" alt="Screenshot 2026-05-03 073911" src="https://github.com/user-attachments/assets/c8dbe1d4-d058-4e00-ab38-53b061ddb38f" /> 
<br>


The Executive Sales Overview dashboard provides a high-level summary of the e-commerce business performance.
The total sales reached 4 million across 250 orders and approximately 2,000 customers, indicating a moderate transaction volume with relatively high-value purchases.

<ins> Payment Insights </ins>

Payment method analysis shows that PayPal (28.56%) and Credit Card (25.26%) are the most preferred options, indicating strong customer trust in digital payment systems.
In contrast, Debit Card usage (13.08%) is relatively low, suggesting an opportunity to promote alternative payment incentives.

<ins> Customer Distribution Insights </ins>

Customer distribution is concentrated in major cities such as Boston, Dallas, Houston, Miami, and New York, each contributing around 180 customers.
However, Los Angeles shows lower customer engagement (~120 customers), indicating a potential market expansion opportunity.

<ins> Revenue by Location </ins>

Sales performance varies significantly by location.
Miami generates the highest revenue (507,200), making it the most valuable market, while San Francisco records the lowest (259,120), suggesting lower customer spending or demand.

<ins> Product Category Insights </ins>

Among product categories, Electronics dominate total sales, highlighting strong demand for tech products.
In contrast, Books generate the lowest revenue, indicating weaker performance and possible need for promotional strategies.


- #### <ins> Key Business Recommendations </ins>

  - Focus marketing efforts on high-performing regions like Miami to maximize revenue.
  - Investigate low-performing markets such as San Francisco and Los Angeles to improve engagement.
  - Promote low-performing categories (Books) through discounts or bundling strategies.
  - Encourage adoption of underused payment methods like Debit Cards through offers or cashback incentives.
  - Leverage the popularity of Electronics by expanding product variety and inventory.

---
### <ins> Page 2 | PRODUCT PERFORMANCE ANALYSIS </ins>

The Product Performance Analysis dashboard evaluates product-level performance by analyzing sales revenue and quantity sold.
It helps identify top-performing products, underperforming items, and overall product demand trends.
<br>
<img width="1293" height="782" alt="Screenshot 2026-05-03 081015" src="https://github.com/user-attachments/assets/12dcad50-7864-4515-a931-c1c53dd77997" />

<br>


Smartwatches recorded the highest quantity sold (1680 units), indicating strong customer demand and popularity.
Washing Machines have the lowest quantity sold (720 units), suggesting lower demand or higher price sensitivity.
In terms of revenue, Refrigerators generated the highest total sales (1,248,000), making them the most valuable product category.
Books generated the lowest revenue (16,560), confirming weak performance in both demand and profitability.


High quantity does not always mean high revenue.
For example, Smartwatches sell in large volumes, but Refrigerators generate more revenue due to higher pricing.
This highlights the difference between volume-driven vs value-driven products.

- #### <ins> Key Business Recommendations </ins>
 - Focus inventory and marketing on high-demand products like Smartwatches to maintain sales volume.
 - Prioritize high-revenue products like Refrigerators for profit maximization.
 - Re-evaluate low-performing products such as Books by introducing promotions or discounts.
 - Analyze why Washing Machines have low demand (price, competition, or customer preference).

---
### <ins> Page 3 | CUSTOMER ANALYTICS DASHBOARD </ins>

The Customer Analytics dashboard focuses on customer purchasing behavior, identifying high-value customers and analyzing order patterns.
This helps in understanding customer contribution to revenue and engagement levels.
<br>
<img width="814" height="710" alt="Screenshot 2026-05-03 081537" src="https://github.com/user-attachments/assets/4f5e3a68-a108-4d00-9390-48b8c2d2ca81" />


<br>

Oliver Winston generated the highest total sales (578,720), making him the most valuable customer.
Emma Clark placed the highest number of orders (32 orders), indicating strong engagement and frequent purchasing behavior.


Not all customers behave the same,

Some customers (like Emma Clark) are frequent buyers
Others (like Oliver Winston) are high spenders

This shows two important customer types:
-- High-frequency customers
-- High-value customers


- #### <ins> Key Business Recommendations </ins>
  - Retain high-value customers like Oliver Winston through loyalty programs and personalized offers.
  - Encourage repeat purchases from customers like Emma Clark with rewards and engagement strategies.
  - Re-engage low-performing customers such as Sophia Miller through targeted promotions or discounts.
  - Segment customers into groups (high-value, frequent, low-engagement) for better marketing strategies.
