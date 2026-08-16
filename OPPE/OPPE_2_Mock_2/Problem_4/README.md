# Consistent Sales Increase

You are given a CSV file with following columns:
`ID,Name,Gender,Region,Q1,Q2,Q3,Q4`

Each row in the file (except header) represents the record of sales representatives, which includes their ID, Name, Gender, Region where they operate, and their sales figure of each quarter.

Define a function named `consistent_sales_increase` that takes `filename` as argument and returns the name of the region with the highest count of representatives whose sales figures are consistently increasing across quarters, i.e. `Q1 < Q2 < Q3 < Q4`.

### Example
Suppose `company_data1.csv` contains data where "Chennai" has the most representatives with strictly increasing quarterly sales.
`consistent_sales_increase("company_data1.csv")` should return `"Chennai"`.
