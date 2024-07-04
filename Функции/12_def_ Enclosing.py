def outer_func ():
    enclosing_var = "Я переменна в охватывающей функции"

    def inner_func ():
         print ( "Внутри вложенной функции:" , enclosing_var)

    inner_func ()

outer_func ()
