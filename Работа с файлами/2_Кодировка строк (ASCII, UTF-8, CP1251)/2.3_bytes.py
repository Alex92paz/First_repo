# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('/Users/alx_it/Documents/Git/First_repo/example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
