fh = open ( 'text.txt' , 'w' )
try :
    # Выполнение операций с файлом 
    fh. write ( 'Some data' )
finally :
    # Закрытие файла в блоке finally гарантирует, что файл закроется даже в случае ошибки 
    fh. close ()
