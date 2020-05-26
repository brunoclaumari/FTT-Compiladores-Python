import re

pascal_code = ""
pascal_keys = ""
pascal_datatype = ""
pascal_operators = ""
pascal_separators=""


with open('p1.pas', "r") as pkeys2:
    pascal_code = pkeys2.read().lower().splitlines()

with open('pascal_keys.txt', "r") as pkeys:
    pascal_keys = pkeys.read().split()

with open('pascal_datatype.txt', "r") as pkeys:
    pascal_datatype = pkeys.read().split()    

with open('pascal_operators.txt', "r") as pkeys:
    pascal_operators = pkeys.read().split() 

with open('pascal_separators.txt', "r") as pkeys:
    pascal_separators = pkeys.read().split()

if '#' in pascal_separators:
    print(['(', 'separator'])
else:
    print('simbolo não encontrado!')    


print(pascal_separators)    

