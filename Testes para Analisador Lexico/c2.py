import re

pascal_keys = ""
pascal_code = ""

with open("pascalkeys.txt", "r") as pkeys:
    pascal_keys = pkeys.read().split()

with open("p1.pas", "r") as pkeys2:
    pascal_code = pkeys2.read().lower().split(' ')

lexemas = []

integerPattern = r"^[0-9]$"  # expressões regulares
floatPattern = r"^[0-9]+.[0-9]+F*$"  # expressões regulares

for token in pascal_code:
    if token in pascal_keys:
        lexemas.append([token, "key word"])
    elif re.match(integerPattern, token):
        lexemas.append([token, "integer"])
    elif re.match(floatPattern, token):
        lexemas.append([token, "float"])
    else:
        lexemas.append([token, "unknow"])

# print(pascal_keys)
# print(pascal_code)
print(lexemas)

with open("tokens.txt", "w") as lexemas_file:
    lexemas_file.write(str(lexemas))

# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping

# TODO: Terminar...
