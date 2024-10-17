def get_fullname (first_name, last_name, middle_name = ""):
    if middle_name != "":
        return (f"{first_name} {middle_name} {last_name}")
    else:
        return (f"{first_name} {last_name}")
    
resolt = get_fullname ('Aleksandr', 'Pozdnikin', 'Michailovihch')
print(resolt)

resolt2 = get_fullname ('Aleksandr', 'Pozdnikin')
print(resolt2)