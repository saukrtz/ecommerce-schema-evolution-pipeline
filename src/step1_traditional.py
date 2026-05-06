import pandas as pd
import os

def run_traditional():
    print("--- Step 1: Traditional Approach (Problem) ---")
    try:
        df1 = pd.read_csv("data/products_day1.csv")
        df2 = pd.read_csv("data/products_day2.csv")
        
        # In simple pandas concat, it actually handles different columns by adding NaNs.
        # However, in many production SQL-based or fixed-schema pipelines, this would fail.
        # We demonstrate the mismatch here.
        print("Day 1 Columns:", df1.columns.tolist())
        print("Day 2 Columns:", df2.columns.tolist())
        
        df = pd.concat([df1, df2], ignore_index=True)
        print("\nMerged DataFrame (Traditional pd.concat):")
        print(df)
        print("\nIssue: Missing values for 'brand' in Day 1 records are now NaN.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_traditional()
