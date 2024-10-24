intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab))
