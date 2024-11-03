fh = open('test.txt' , 'w') 
fh.write('привет!')
fh.close( ) 
fh = open ('test.txt' , 'r')
all_file = fh.read ()
print (all_file) # 'привет!' 
fh.close ( )


