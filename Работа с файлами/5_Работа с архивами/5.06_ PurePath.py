from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

# У PurePath є ряд корисних методів та атрибутів:

# p.parent вказує на батьківську директорію;
# p.name повертає лише рядок з ім'ям директорі або файлу, на який вказує p;
# p.suffix повертає рядком розширення файлу, на який вказує p, починаючи з крапки;