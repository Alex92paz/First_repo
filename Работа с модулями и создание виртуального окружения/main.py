# main.py
import mymodule

print(mymodule.say_hello("World"))


# main.py
from mymodule import say_hello

print(say_hello("World"))


# main.py
from mymodule import say_hello as greeting

print(greeting("World"))


# from module_name import item_name as alias
