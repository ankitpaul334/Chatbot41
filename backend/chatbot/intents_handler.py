def handle_query(query, data):
    if "top" in query.lower() and "sold" in query.lower():
        top_products = data['products'].nlargest(5, 'units_sold')
        return top_products[['product_name', 'units_sold']].to_dict(orient="records")
    elif "status" in query.lower() and "order" in query.lower():
        order_id = ''.join(filter(str.isdigit, query))
        order = data['orders'][data['orders']['order_id'] == int(order_id)]
        if not order.empty:
            return {"status": order.iloc[0]['status']}
        return "Order ID not found."
    elif "stock" in query.lower():
        product_name = "Classic T-Shirt"
        stock = data['products'][data['products']['product_name'].str.contains(product_name, case=False)]
        if not stock.empty:
            return {"in_stock": int(stock.iloc[0]['stock'])}
        return "Product not found in stock."
    else:
        return "Sorry, I didn't understand your question."
