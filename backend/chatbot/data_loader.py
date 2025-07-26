import os
import pandas as pd
from pymongo import MongoClient

print("🚀 Script started")

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]
products_collection = db["products"]
orders_collection = db["orders"]
print("🧩 Connected to MongoDB")

# Define path to CSVs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "..", "data")
products_path = os.path.join(data_dir, "products.csv")
orders_path = os.path.join(data_dir, "orders.csv")

print(f"📂 Products path: {products_path}")
print(f"📂 Orders path: {orders_path}")

def load_data():
    try:
        # Load Products
        products_df = pd.read_csv(products_path)
        products_collection.delete_many({})
        products_collection.insert_many(products_df.to_dict(orient="records"))
        print("✅ Products data loaded into MongoDB.")

        # Load Orders
        orders_df = pd.read_csv(orders_path)
        orders_collection.delete_many({})
        orders_collection.insert_many(orders_df.to_dict(orient="records"))
        print("✅ Orders data loaded into MongoDB.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")

if __name__ == "__main__":
    load_data()
