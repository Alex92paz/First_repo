from collections import defaultdict

d = defaultdict( int ) # Увеличение значения для каждого ключа 
d[ 'a' ] += 1 
d[ 'b' ] += 1 
d[ 'a' ] += 1 

print(d)




