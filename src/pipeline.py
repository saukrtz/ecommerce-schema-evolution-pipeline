import pandas as pd
import os

def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"Warning: {file_path} not found.")
        return pd.DataFrame()

def merge_schemas(dfs):
    """
    Concatenates a list of DataFrames. 
    Pandas handles schema evolution by aligning columns and filling missing values with NaN.
    """
    return pd.concat(dfs, ignore_index=True)

def handle_missing_values(df):
    """
    Implements Step 6: Handle Missing Values
    Fills 'brand' with 'Unknown' and 'discount' with 0.
    """
    # Use fillna with a dictionary for efficiency
    fill_values = {
        "brand": "Unknown",
        "discount": 0
    }
    
    # Only fill if the column exists
    for col, val in fill_values.items():
        if col in df.columns:
            df[col] = df[col].fillna(val)
    
    return df

def run_full_pipeline():
    print("--- Step 7: Running Full Schema Evolution Pipeline ---")
    
    # Load all days
    df1 = load_data("data/products_day1.csv")
    df2 = load_data("data/products_day2.csv")
    df3 = load_data("data/products_day3.csv")
    
    # Merge all
    df = merge_schemas([df1, df2, df3])
    
    print(f"\nColumns after merge: {df.columns.tolist()}")
    
    # Clean/Handle Missing Values
    df = handle_missing_values(df)
    
    # Save final result
    output_path = "data/final_products.csv"
    df.to_csv(output_path, index=False)
    
    print(f"\nFinal Pipeline Output (first 10 rows):")
    print(df.head(10))
    print(f"\nPipeline complete. Results saved to {output_path}")
    return df

if __name__ == "__main__":
    run_full_pipeline()
