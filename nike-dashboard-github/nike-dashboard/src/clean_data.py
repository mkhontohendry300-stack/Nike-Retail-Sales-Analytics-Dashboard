"""
Nike Sales Data Cleaning Script
================================
Capaciti Data Analytics Programme
Author: Malehu Segoapa

Description:
    Cleans the raw Nike Sales dataset and exports a clean Excel file
    ready for Power BI import.

Input:  data/Nike_Sales_Raw.csv
Output: data/Nike_Sales_Clean.csv
        data/Nike_Sales_Clean.xlsx

Usage:
    python src/clean_data.py
"""

import pandas as pd
import numpy as np
from dateutil import parser as dateparser


# ── CONFIG ────────────────────────────────────────────────────────────────────
INPUT_FILE  = 'data/Nike_Sales_Raw.csv'
OUTPUT_CSV  = 'data/Nike_Sales_Clean.csv'
OUTPUT_XLSX = 'data/Nike_Sales_Clean.xlsx'


# ── REGION MAP ────────────────────────────────────────────────────────────────
REGION_MAP = {
    'bengaluru': 'Bangalore',
    'Bangalore': 'Bangalore',
    'hyderbad':  'Hyderabad',
    'Hyd':       'Hyderabad',
    'Hyderabad': 'Hyderabad',
    'Mumbai':    'Mumbai',
    'Delhi':     'Delhi',
    'Pune':      'Pune',
    'Kolkata':   'Kolkata',
}


# ── DATE PARSER ───────────────────────────────────────────────────────────────
def parse_date(val):
    """Parse dates from multiple formats into a single standard format."""
    if pd.isnull(val):
        return pd.NaT
    try:
        return dateparser.parse(str(val), dayfirst=False)
    except Exception:
        return pd.NaT


# ── MAIN CLEANING FUNCTION ───────────────────────────────────────────────────
def clean_data(input_path: str) -> pd.DataFrame:
    print(f"📂 Loading: {input_path}")
    df = pd.read_csv(input_path)
    print(f"   Raw shape: {df.shape}")

    # 1. Remove duplicate Order IDs
    before = len(df)
    df = df.drop_duplicates(subset='Order_ID', keep='first')
    print(f"✅ Step 1 — Removed {before - len(df)} duplicate Order IDs")

    # 2. Fix Region typos
    df['Region'] = df['Region'].str.strip().map(REGION_MAP).fillna(df['Region'])
    print(f"✅ Step 2 — Fixed Region typos → {df['Region'].unique().tolist()}")

    # 3. Parse and standardize Order_Date
    df['Order_Date'] = df['Order_Date'].apply(parse_date)
    before = len(df)
    df = df.dropna(subset=['Order_Date'])
    print(f"✅ Step 3 — Removed {before - len(df)} rows with invalid dates")
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])

    # 4. Fix Size nulls
    df['Size'] = df['Size'].fillna('Unknown')
    print(f"✅ Step 4 — Filled Size nulls with 'Unknown'")

    # 5. Fix Units_Sold — fill nulls and remove negatives
    df['Units_Sold'] = df['Units_Sold'].fillna(0)
    df['Units_Sold'] = df['Units_Sold'].clip(lower=0)
    df['Units_Sold'] = df['Units_Sold'].astype(int)
    print(f"✅ Step 5 — Fixed Units_Sold (nulls→0, negatives→0, int type)")

    # 6. Fix MRP
    df['MRP'] = pd.to_numeric(df['MRP'], errors='coerce').fillna(0).round(2)
    print(f"✅ Step 6 — Fixed MRP (nulls→0)")

    # 7. Fix Discount_Applied — fill nulls and cap at 1.0
    df['Discount_Applied'] = pd.to_numeric(df['Discount_Applied'], errors='coerce').fillna(0)
    df['Discount_Applied'] = df['Discount_Applied'].clip(lower=0, upper=1.0).round(4)
    print(f"✅ Step 7 — Fixed Discount_Applied (nulls→0, capped at 1.0)")

    # 8. Fix Revenue — fill nulls and remove negatives
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce').fillna(0).round(2)
    df['Revenue'] = df['Revenue'].clip(lower=0)
    print(f"✅ Step 8 — Fixed Revenue (nulls→0, negatives→0)")

    # 9. Fix Profit — keep negatives (legitimate losses)
    df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce').fillna(0).round(2)
    print(f"✅ Step 9 — Fixed Profit (nulls→0, negatives kept)")

    # 10. Add helper columns for Power BI
    df['Month_Year']   = df['Order_Date'].dt.strftime('%Y-%m')
    df['Year']         = df['Order_Date'].dt.year.astype(int)
    df['Month_Number'] = df['Order_Date'].dt.month.astype(int)
    df['Month_Name']   = df['Order_Date'].dt.strftime('%b')
    print(f"✅ Step 10 — Added Month_Year, Year, Month_Number, Month_Name columns")

    # Format Order_Date as string for CSV
    df['Order_Date'] = df['Order_Date'].dt.strftime('%Y-%m-%d')

    print(f"\n📊 Final shape: {df.shape}")
    print(f"   Columns: {list(df.columns)}")

    # Quality check
    print("\n🔍 Quality Check — Nulls in numeric columns:")
    numeric_cols = ['Units_Sold', 'MRP', 'Discount_Applied', 'Revenue', 'Profit']
    for col in numeric_cols:
        print(f"   {col}: {df[col].isnull().sum()} nulls | dtype: {df[col].dtype}")

    return df


# ── SAVE FUNCTION ─────────────────────────────────────────────────────────────
def save_outputs(df: pd.DataFrame):
    # Save CSV
    df.to_csv(OUTPUT_CSV, index=False, float_format='%.2f')
    print(f"\n💾 Saved CSV:   {OUTPUT_CSV}")

    # Save Excel with proper data types
    df_xlsx = df.copy()
    df_xlsx['Order_Date'] = pd.to_datetime(df_xlsx['Order_Date'])

    with pd.ExcelWriter(OUTPUT_XLSX, engine='openpyxl') as writer:
        df_xlsx.to_excel(writer, index=False, sheet_name='Nike_Sales_Clean')

    print(f"💾 Saved Excel: {OUTPUT_XLSX}")
    print(f"\n✅ All done! {len(df):,} clean rows ready for Power BI.")


# ── RUN ───────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    df_clean = clean_data(INPUT_FILE)
    save_outputs(df_clean)
