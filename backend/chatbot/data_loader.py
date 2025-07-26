import os
import pandas as pd
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]

# Define path to CSVs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "..", "data")

products_path = os.path.join(data_dir, "products.csv")
orders_path = os.path.join(data_dir, "orders.csv")

# Load CSVs
try:
    products_df = pd.read_csv(products_path)
    orders_df = pd.read_csv(orders_path)

    # Insert into MongoDB
    db.products.delete_many({})
    db.orders.delete_many({})

    db.products.insert_many(products_df.to_dict(orient="records"))
    db.orders.insert_many(orders_df.to_dict(orient="records"))

    print("✅ Data loaded successfully into MongoDB.")

except Exception as e:
    print(f"❌ Failed to load data: {e}")
