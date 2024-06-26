pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")

'''
В цьому випадку виведення буде "There's a dog.",
бо тільки "dog" знаходиться на своєму місці. Тут
match використовується для перевірки, чи містить
список pets певні комбінації тварин. Причому важливо,
що саме комбінації, і саме тому в нас спрацював
case ["dog", _, _]:, а не case ["dog", "cat", _]:,
бо cat в списку pets знаходиться в кінці, а не після dog.
Знак _ в шаблоні використовується як "заповнювач", що означає
"будь-яке інше значення".
'''