def  modify_string ( original: str ) -> str :
    original = "изменен" 
    return original

str_var = "оригинал" 
print (modify_string(str_var))   # выведет: изменен 
print (str_var)                 # выведет: оригинал
