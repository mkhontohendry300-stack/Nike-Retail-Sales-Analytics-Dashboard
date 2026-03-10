# 📐 DAX Measures — Nike Sales Dashboard

All 13 measures used in the Power BI dashboard.
Table name: `Nike_Sales_Clean`

---

## Core KPIs

```dax
Total Revenue = SUM(Nike_Sales_Clean[Revenue])
```

```dax
Total Profit = SUM(Nike_Sales_Clean[Profit])
```

```dax
Total Units Sold = SUM(Nike_Sales_Clean[Units_Sold])
```

```dax
Total Orders = DISTINCTCOUNT(Nike_Sales_Clean[Order_ID])
```

```dax
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0) * 100
```

```dax
Avg Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

```dax
Avg Discount % = AVERAGE(Nike_Sales_Clean[Discount_Applied]) * 100
```

---

## Sales Channel

```dax
Online Revenue = CALCULATE([Total Revenue], Nike_Sales_Clean[Sales_Channel] = "Online")
```

```dax
Retail Revenue = CALCULATE([Total Revenue], Nike_Sales_Clean[Sales_Channel] = "Retail")
```

```dax
Online Revenue % = DIVIDE([Online Revenue], [Total Revenue], 0) * 100
```

---

## Profit Health

```dax
Profitable Orders = CALCULATE([Total Orders], Nike_Sales_Clean[Profit] > 0)
```

```dax
Loss Orders = CALCULATE([Total Orders], Nike_Sales_Clean[Profit] < 0)
```

---

## Time Intelligence

```dax
YTD Revenue = TOTALYTD([Total Revenue], Nike_Sales_Clean[Order_Date])
```
