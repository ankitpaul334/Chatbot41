def handle_query(query, data):
    products = data['products']
    orders = data['orders']

    if "top" in query.lower() and "sold" in query.lower():
        top_products = products.find().sort("units_sold", -1).limit(5)
        return [{"product_name": p["product_name"], "units_sold": p["units_sold"]} for p in top_products]

    elif "status" in query.lower() and "order" in query.lower():
        order_id = ''.join(filter(str.isdigit, query))
        order = orders.find_one({"order_id": int(order_id)})
        if order:
            return {"status": order["status"]}
        return "Order ID not found."

    elif "stock" in query.lower():
        product_name = "Classic T-Shirt"
        product = products.find_one({"product_name": {"$regex": product_name, "$options": "i"}})
        if product:
            return {"in_stock": product["stock"]}
        return "Product not found in stock."

    else:
        return "Sorry, I didn't understand your question."
