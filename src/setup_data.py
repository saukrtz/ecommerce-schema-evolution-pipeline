import pandas as pd
import os

def create_datasets():
    os.makedirs("data", exist_ok=True)
    
    # Day 1: Basic schema
    day1_data = {
        "product_id": [1, 2, 3],
        "name": ["Laptop", "Shoes", "Phone"],
        "category": ["Electronics", "Fashion", "Electronics"],
        "price": [800, 100, 500]
    }
    df1 = pd.DataFrame(day1_data)
    df1.to_csv("data/products_day1.csv", index=False)
    print("Created data/products_day1.csv")

    # Day 2: Schema Changed (Added 'brand')
    day2_data = {
        "product_id": [4, 5],
        "name": ["Tablet", "Watch"],
        "category": ["Electronics", "Fashion"],
        "price": [300, 150],
        "brand": ["Samsung", "Fossil"]
    }
    df2 = pd.DataFrame(day2_data)
    df2.to_csv("data/products_day2.csv", index=False)
    print("Created data/products_day2.csv")

    # Day 3: Another Change (Added 'discount')
    day3_data = {
        "product_id": [6],
        "name": ["TV"],
        "category": ["Electronics"],
        "price": [1000],
        "brand": ["Sony"],
        "discount": [10]
    }
    df3 = pd.DataFrame(day3_data)
    df3.to_csv("data/products_day3.csv", index=False)
    print("Created data/products_day3.csv")

if __name__ == "__main__":
    create_datasets()
