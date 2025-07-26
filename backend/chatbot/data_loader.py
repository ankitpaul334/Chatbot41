import pandas as pd

def load_data():
    products = pd.read_csv("path/to/products.csv")
    orders = pd.read_csv("path/to/orders.csv")
    return {
        "products": products,
        "orders": orders
    }
 
