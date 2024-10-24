import re 

text = "apple#banana!mango@orange;kiwi" 
pattern = r"[#@;!]" 
fruits = re.split(pattern, text)
print(fruits)

'''
В этом примере [#@;!]создается набор символов, включающий #, @, ;, и !,
каждый из которых может быть использован в качестве разделителя
'''