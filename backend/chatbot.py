import pandas as pd
import os

class Chatbot:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.products = pd.read_csv(os.path.join(data_dir, "products.csv"))
        self.orders = pd.read_csv(os.path.join(data_dir, "orders.csv"))
        self.order_items = pd.read_csv(os.path.join(data_dir, "order_items.csv"))
        self.inventory = pd.read_csv(os.path.join(data_dir, "inventory_items.csv"))
        # Add more as needed

    def handle_message(self, message: str) -> str:
        m = message.lower()

        if "top" in m and "sell" in m:
            return self.top_sold_products()

        if "status of order" in m or "order status" in m:
            return self.order_status_by_id(self.extract_digits(m))

        if "left in stock" in m or "stock" in m:
            return self.stock_check(m)

        return "Sorry, I didn't understand that question. Please ask about popular products, stock, or order status."

    def top_sold_products(self, n=5) -> str:
        sales = (self.order_items.groupby('product_id')
                 .size()
                 .reset_index(name='sold_count')
                 .sort_values(by='sold_count', ascending=False)
                 .head(n))
        merged = sales.merge(self.products, left_on='product_id', right_on='id')
        return "Top sold products:\n" + "\n".join(
            f"{row['name']} ({int(row['sold_count'])} sold)" for _, row in merged.iterrows()
        )

    def order_status_by_id(self, order_id) -> str:
        try:
            order_id = int(order_id)
        except:
            return "Please provide a valid order ID (number)."
        res = self.orders[self.orders['order_id'] == order_id]
        if res.empty:
            return f"No order found with ID {order_id}."
        status = res.iloc[0]['status']
        return f"Order {order_id} status: {status}"

    def stock_check(self, m) -> str:
        # Extract product name (simple heuristic)
        for prod in self.products["name"]:
            if prod.lower() in m:
                prod_name = prod
                break
        else:
            return "Which product do you want to know about?"

        # Remaining in stock = items not sold (sold_at is NaN in inventory)
        prod_id = self.products[self.products["name"] == prod_name]["id"].values[0]
        in_stock = self.inventory[(self.inventory["product_id"] == prod_id) & (self.inventory["sold_at"].isnull())]
        num = len(in_stock)
        return f"There are {num} {prod_name}s left in stock."

    def extract_digits(self, s):
        import re
        found = re.findall(r'\d+', s)
        return found[0] if found else None
