import pandas as pd

def detect_and_merge():
    print("--- Step 3 & 4: Auto Schema Detection & Merge ---")
    df1 = pd.read_csv("data/products_day1.csv")
    df2 = pd.read_csv("data/products_day2.csv")

    # Detect new columns
    new_cols = set(df2.columns) - set(df1.columns)
    print(f"Detected new columns in Day 2: {new_cols}")

    # Merge schemas (Pandas does this automatically with concat, but we explicitly track it)
    df = pd.concat([df1, df2], ignore_index=True)
    
    print("\nDataFrame after Day 2 Merge:")
    print(df)
    return df

if __name__ == "__main__":
    detect_and_merge()
