import re

text = "Se puede aprender a programar en Python porque es un leguaje sencillo."

pattern = r'\bPython\b'

match = re.search(pattern, text)

print(type(match))

if match:
    print("Se encontró la palabra", match.group())
else:
    print("La palabra no fue encontrada.")  