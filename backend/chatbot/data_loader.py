if __name__ == "__main__":
    print("[INFO] Running data_loader.py...")

    from pymongo import MongoClient
    import pandas as pd

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["chatbot"]

    print("[INFO] Connected to MongoDB")

    # Load and insert products
    products_df = pd.read_csv("products.csv")
    db.products.delete_many({})
    db.products.insert_many(products_df.to_dict(orient="records"))
    print(f"[INFO] Inserted {len(products_df)} products.")

    # Load and insert orders
    orders_df = pd.read_csv("orders.csv")
    db.orders.delete_many({})
    db.orders.insert_many(orders_df.to_dict(orient="records"))
    print(f"[INFO] Inserted {len(orders_df)} orders.")

    print("[SUCCESS] Data loading complete.")
