def first(size, *args):
    return size + len(args)
    
def second(size, **kwargs):
    return size + len(kwargs)

print(first(10,"Alex", "Orel", "Block"))
print(second(2, Model_Car = 'Electro', Type_of_animal = 'Cat'))