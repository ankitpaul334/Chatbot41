import pandas as pd
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

# CSV file paths relative to backend/chatbot/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../../ecommerce-dataset")

products_path = os.path.join(DATA_DIR, "products.csv")
orders_path = os.path.join(DATA_DIR, "orders.csv")
inventory_path = os.path.join(DATA_DIR, "inventory.csv")

# Load CSVs into pandas
products_df = pd.read_csv(products_path)
orders_df = pd.read_csv(orders_path)
inventory_df = pd.read_csv(inventory_path)

# Clean insert (remove old)
db.products.delete_many({})
db.orders.delete_many({})
db.inventory.delete_many({})

# Insert into MongoDB
db.products.insert_many(products_df.to_dict("records"))
db.orders.insert_many(orders_df.to_dict("records"))
db.inventory.insert_many(inventory_df.to_dict("records"))

print("✅ Data loaded into MongoDB successfully!")
