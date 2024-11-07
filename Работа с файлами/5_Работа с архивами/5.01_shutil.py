import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='/Users/alx_it/Documents/Git/First_repo/Работа с файлами/1_Работа с файлами и обработка исключений')


shutil.make_archive('/Users/alx_it/Documents/Git/First_repo/Работа с файлами/5_Работа с архивами/example','zip', 
    root_dir='/Users/alx_it/Documents/Git/First_repo/Работа с файлами/1_Работа с файлами и обработка исключений'
)