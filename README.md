#  Nike Sales Performance Dashboard
### Power BI | Data Analytics | India Region | FY 2023–2025

<img width="1402" height="630" alt="image" src="https://github.com/user-attachments/assets/05da0e81-b2fc-4f43-8694-d44f754424f5" />


---

##  Project Overview

A full end-to-end data analytics project built in **Power BI Desktop**, covering data cleaning, DAX measure creation, and interactive dashboard design using Nike sales data across 6 Indian cities.

This project demonstrates:
- Raw data cleaning and transformation
- DAX measure creation
- Interactive Power BI dashboard design
- Nike brand-themed visual storytelling

---

##  Project Structure

```
nike-dashboard/
│
├── data/
│   ├── Nike_Sales_Raw.csv          ← Original uncleaned dataset
│   ├── Nike_Sales_Clean.csv        ← Cleaned CSV
│   └── Nike_Sales_Clean.xlsx       ← Final Excel file (used in Power BI)
│
├── docs/
│   ├── data_cleaning_report.md     ← All cleaning steps documented
│   ├── dax_measures.md             ← All 13 DAX measures
│   └── insights_report.md          ← Key findings and insights
│
├── src/
│   └── clean_data.py               ← Python data cleaning script
│
├── screenshots/
│   └── dashboard.png               ← Dashboard screenshot
│
└── README.md                       ← This file
```

---

##  Dashboard Visuals

| # | Visual | Type | Purpose |
|---|--------|------|---------|
| 1 | Total Revenue | KPI Card | Headline revenue figure |
| 2 | Total Profit | KPI Card | Overall profit |
| 3 | Total Orders | KPI Card | Unique order count |
| 4 | Profit Margin % | KPI Card | Profit as % of revenue |
| 5 | Revenue by Region | Bar Chart | City-level performance |
| 6 | Revenue Over Time | Line Chart | Monthly trend analysis |
| 7 | Revenue by Product Line | Donut Chart | Category breakdown |
| 8 | Profit vs Loss Orders | Stacked Bar | Order health by channel |
| 9 | Top Products Table | Table | Product ranking |
| 10 | Gender Breakdown | Pie Chart | Units sold by gender |
| 11 | Online vs Retail | Clustered Bar | Channel comparison |

---

##  Key Metrics

| Metric | Value |
|--------|-------|
| Total Revenue | 622,074 |
| Total Profit | 2,483,123 |
| Total Orders | 1,804 |
| Total Units Sold | 1,528 |
| Profit Margin % | 399.2% |
| Date Range | Jul 2023 – Dec 2025 |
| Regions | 6 Indian Cities |
| Sales Channels | Online & Retail |

---

##  Key Insights

- **Kolkata** is the top performing region with **134,520** in revenue
- **Training** is the best selling product line at **26.8%** of total revenue
- **LeBron 20** is the #1 product with **63,676** in revenue
- **Online** (322K) slightly outperforms **Retail** (299K) in revenue
- Gender split is nearly equal: **Men 34%**, **Kids 33%**, **Women 33%**
- **December 2024** was the best month at **66,961** in revenue
- **1,385** profitable orders vs **419** loss orders

---

##  Tools Used

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning |
| Power BI Desktop | Dashboard & visualizations |
| DAX | Calculated measures |
| Excel | Final data format for Power BI |

---

##  Data Cleaning Summary

The raw dataset had **14 quality issues** that were fixed:

1. ✅ Removed 114 duplicate Order IDs
2. ✅ Fixed 3 mixed date formats → standardized to YYYY-MM-DD
3. ✅ Removed 582 rows with unparseable dates
4. ✅ Fixed Region typos (bengaluru → Bangalore, Hyd → Hyderabad)
5. ✅ Filled 510 missing Size values → "Unknown"
6. ✅ Filled 1,235 missing Units_Sold → 0
7. ✅ Fixed 205 negative Units_Sold → 0
8. ✅ Filled 1,254 missing MRP → 0
9. ✅ Filled 1,668 missing Discount values → 0
10. ✅ Capped 180 discounts over 100% → 1.0
11. ✅ Fixed 53 negative Revenue values → 0
12. ✅ Added Month_Year, Year, Month_Number, Month_Name columns
13. ✅ Ensured all numeric columns have zero nulls
14. ✅ Exported as Excel to ensure correct data types in Power BI

**Final dataset: 1,804 clean rows | 17 columns | 0 nulls in numeric columns**

---

##  How to Use

1. Clone this repository
2. Open Power BI Desktop
3. Go to **Home → Get Data → Excel Workbook**
4. Select `data/Nike_Sales_Clean.xlsx`
5. Click **Load**
6. Create the 13 DAX measures from `docs/dax_measures.md`
7. Build the visuals following the dashboard layout

---

##  DAX Measures

See [`docs/dax_measures.md`](docs/dax_measures.md) for all 13 measures.

---

##  Author

**Mkhonto Hendry Mike**
Data Analytics 
Mkhontohendry300@gmail.com

---

##  License

