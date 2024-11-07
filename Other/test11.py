product_name = "Coffee Maker"
product_price = 7500.50
product_quantity = 15

def format_product_info():
    product_info = f"Product: {product_name}, Price: {product_price} UAH, Quantity: {product_quantity} pcs."
    return product_info

# Вызов функции и сохранение результата
product_info = format_product_info()

# Вывод результата
print(product_info)
