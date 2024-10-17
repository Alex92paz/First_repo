def discount_price(price, discount):

    def apply_discount():
        nonlocal price, discount
        price = price * (1 - discount)

    apply_discount()
    return price

total_coast = discount_price(110.74, 0.72)
print(round(total_coast,2))

total_coast = discount_price(234.88, 0.52)
print(round(total_coast,2))
