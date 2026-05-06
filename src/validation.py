import pandas as pd

def validate_results():
    print("--- Step 9: Validation ---")
    df = pd.read_csv("data/final_products.csv")
    
    print("\nColumn List:")
    print(df.columns.tolist())
    
    print("\nMissing Values Count:")
    print(df.isnull().sum())
    
    # Check if 'Unknown' and '0' are correctly filled
    print("\nSummary of 'brand' distribution:")
    print(df['brand'].value_counts())
    
    print("\nSummary of 'discount' values:")
    print(df['discount'].unique())

if __name__ == "__main__":
    validate_results()
