# 🧹 Data Cleaning Report — Nike Sales Dataset

## Overview

| Item | Value |
|------|-------|
| Raw Dataset | Nike_Sales_Raw.csv |
| Raw Rows | 2,500 |
| Final Rows | 1,804 |
| Rows Removed | 696 |
| Raw Columns | 13 |
| Final Columns | 17 |
| Tool Used | Python (Pandas) |

---

## Issues Found in Raw Data

| # | Column | Issue | Count |
|---|--------|-------|-------|
| 1 | Order_ID | Duplicate records | 114 |
| 2 | Order_Date | Null values | 616 |
| 3 | Order_Date | Mixed formats (YYYY-MM-DD, DD-MM-YYYY, YYYY/MM/DD) | Multiple |
| 4 | Region | Typos: bengaluru, Hyd, hyderbad | 497 |
| 5 | Size | Null values | 510 |
| 6 | Units_Sold | Null values | 1,235 |
| 7 | Units_Sold | Negative values | 205 |
| 8 | MRP | Null values | 1,254 |
| 9 | Discount_Applied | Null values | 1,668 |
| 10 | Discount_Applied | Values over 100% (>1.0) | 180 |
| 11 | Revenue | Negative values | 53 |
| 12 | All numeric cols | Float stored as object/string | Multiple |
| 13 | — | Missing helper date columns | — |
| 14 | — | No Year/Month columns for Power BI | — |

---

## Fixes Applied

### 1. Duplicate Order IDs
```python
df = df.drop_duplicates(subset='Order_ID', keep='first')
# Removed 114 duplicate rows
```

### 2. Date Standardization
```python
from dateutil import parser as dateparser

def parse_date(val):
    if pd.isnull(val): return pd.NaT
    try: return dateparser.parse(str(val), dayfirst=False)
    except: return pd.NaT

df['Order_Date'] = df['Order_Date'].apply(parse_date)
df = df.dropna(subset=['Order_Date'])  # removed 582 unparseable rows
df['Order_Date'] = pd.to_datetime(df['Order_Date']).dt.strftime('%Y-%m-%d')
```

### 3. Region Typos
```python
region_map = {
    'bengaluru': 'Bangalore',
    'Bangalore': 'Bangalore',
    'hyderbad':  'Hyderabad',
    'Hyd':       'Hyderabad',
    'Hyderabad': 'Hyderabad',
}
df['Region'] = df['Region'].str.strip().map(region_map).fillna(df['Region'])
```

### 4. Size Nulls
```python
df['Size'] = df['Size'].fillna('Unknown')
```

### 5. Units Sold
```python
df['Units_Sold'] = df['Units_Sold'].fillna(0)
df['Units_Sold'] = df['Units_Sold'].clip(lower=0)  # remove negatives
df['Units_Sold'] = df['Units_Sold'].astype(int)
```

### 6. MRP
```python
df['MRP'] = pd.to_numeric(df['MRP'], errors='coerce').fillna(0).round(2)
```

### 7. Discount Applied
```python
df['Discount_Applied'] = pd.to_numeric(df['Discount_Applied'], errors='coerce').fillna(0)
df['Discount_Applied'] = df['Discount_Applied'].clip(lower=0, upper=1.0).round(4)
```

### 8. Revenue
```python
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce').fillna(0).round(2)
df['Revenue'] = df['Revenue'].clip(lower=0)  # remove negatives
```

### 9. Added Helper Columns
```python
df['Month_Year']   = df['Order_Date'].dt.strftime('%Y-%m')
df['Year']         = df['Order_Date'].dt.year.astype(int)
df['Month_Number'] = df['Order_Date'].dt.month.astype(int)
df['Month_Name']   = df['Order_Date'].dt.strftime('%b')
```

---

## Final Dataset Quality

| Column | Type | Nulls | Min | Max |
|--------|------|-------|-----|-----|
| Order_ID | int64 | 0 | 2000 | 4499 |
| Gender_Category | str | 0 | — | — |
| Product_Line | str | 0 | — | — |
| Product_Name | str | 0 | — | — |
| Size | str | 0 | — | — |
| Units_Sold | int64 | 0 | 0 | 4 |
| MRP | float64 | 0 | 0.0 | 9996.22 |
| Discount_Applied | float64 | 0 | 0.0 | 1.0 |
| Revenue | float64 | 0 | 0.0 | 26105.37 |
| Order_Date | str | 0 | 2023-07-26 | 2025-12-07 |
| Sales_Channel | str | 0 | — | — |
| Region | str | 0 | — | — |
| Profit | float64 | 0 | -1199.32 | 3999.21 |
| Month_Year | str | 0 | — | — |
| Year | int64 | 0 | 2023 | 2025 |
| Month_Number | int64 | 0 | 1 | 12 |
| Month_Name | str | 0 | — | — |
