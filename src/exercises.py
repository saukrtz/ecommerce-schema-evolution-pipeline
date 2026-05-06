import pandas as pd
import os

def run_exercises():
    print("--- Lab Exercises: Schema Evolution Scenarios ---")
    
    # Load base data (Day 1, 2, 3)
    df_base = pd.read_csv("data/final_products.csv")
    
    # --- Exercise 1: Add Column 'rating' ---
    print("\n[Exercise 1] Adding 'rating' column (Day 4 simulation)...")
    day4_data = {
        "product_id": [7, 8],
        "name": ["Speaker", "Keyboard"],
        "category": ["Electronics", "Electronics"],
        "price": [50, 45],
        "brand": ["JBL", "Logitech"],
        "discount": [5, 0],
        "rating": [4.5, 4.2]
    }
    df4 = pd.DataFrame(day4_data)
    
    # Evolve pipeline to handle rating
    df_evolved = pd.concat([df_base, df4], ignore_index=True)
    df_evolved["rating"] = df_evolved["rating"].fillna(0.0) # Impute missing ratings for old records
    print("Columns after adding rating:", df_evolved.columns.tolist())
    
    # --- Exercise 2: Remove Column 'price' safely ---
    print("\n[Exercise 2] Removing 'price' column safely (Day 5 simulation)...")
    # Simulation: A new source file arrives without the 'price' column
    day5_data = {
        "product_id": [9],
        "name": ["Mouse Pad"],
        "category": ["Electronics"],
        "brand": ["Razer"],
        "discount": [0],
        "rating": [4.0]
    }
    df5 = pd.DataFrame(day5_data)
    
    # Concatenate safely - price will be NaN for Day 5
    df_evolved = pd.concat([df_evolved, df5], ignore_index=True)
    print("Price column status (is it still there?):", "price" in df_evolved.columns)
    print("Day 5 record price value:", df_evolved.iloc[-1]["price"])
    
    # --- Exercise 3: Type Change (price from int/float to string) ---
    print("\n[Exercise 3] Handling Type Change (price to string)...")
    # Simulation: A new source file has 'price' as a string with currency
    day6_data = {
        "product_id": [10],
        "name": ["USB Cable"],
        "category": ["Electronics"],
        "price": ["$10"], # String type
        "brand": ["Generic"],
        "discount": [0],
        "rating": [3.5]
    }
    df6 = pd.DataFrame(day6_data)
    
    # To handle this safely, we should cast existing price to string or clean incoming data
    # Method: Standardize all prices to numeric after stripping symbols
    def clean_price(val):
        if isinstance(val, str) and "$" in val:
            return float(val.replace("$", ""))
        return val

    df6["price"] = df6["price"].apply(clean_price)
    
    # Now merge
    df_final = pd.concat([df_evolved, df6], ignore_index=True)
    print("Final columns:", df_final.columns.tolist())
    print("Final price types:", df_final["price"].dtype)
    
    df_final.to_csv("data/final_products_evolved.csv", index=False)
    print("\nExercises complete. Final evolved dataset saved.")

if __name__ == "__main__":
    run_exercises()
