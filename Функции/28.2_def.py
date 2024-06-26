def discount_price(price, discount):
    # Вложенная функция для применения скидки
    def apply_discount():
        nonlocal price  # Используем nonlocal для доступа к переменной price из внешней функции
        price = price * (1 - discount)  # Рассчитываем новую цену после скидки

    apply_discount()  # Вызываем вложенную функцию для применения скидки
    return price  # Возвращаем измененную цену

# Пример вызова функции
initial_price = 100.0  # Начальная цена товара
discount_rate = 0.2  # Скидка 20% (0.2)
final_price = discount_price(initial_price, discount_rate)  # Получаем конечную цену
print(f"Цена после скидки: {final_price}")  # Выводим конечную цену
