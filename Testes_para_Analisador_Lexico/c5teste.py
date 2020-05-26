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




lexemas = []

palavraSemEspaco = r"^([a-zA-Z0-9_\S+]+)$"
spaceWhitePattern = r"^(\s+)$"
#spaceWhitePattern = r"^([\s\s]+)$"
integerPattern = r"^([ ]?[+/-]?[0-9]+[;]?)$"  # expressões regulares
# expressões regulares
realPattern = r"^([ ]?[+/-]?[0-9]+[.][0-9]*[[E/e]?[+/-]?[0-9]+]?[ ]*[;]?)|([ ]?[+/-]?[0-9]*[.][0-9]+[ ]*[;]?)$"

testandoPascal = []

'''for linhaCodigo in pascal_code:
    for item in linhaCodigo:
        for token in pascal_keys:
            #if token == item:
            #lexemas.append([token, "key word"])
            if re.match(integerPattern, token):
                lexemas.append([token, "integer"])
            elif re.match(floatPattern, token):
                lexemas.append([token, "float"])
            else:
                lexemas.append([token, "unknow"])
                
                
                pascalCortado.append(lt.casefold()
        .replace('(',' ( ')
        .replace(')',' ) ')
        .replace(';',' ;'))
                
                '''




for linhas in pascal_code:
    testandoPascal.append(linhas.lstrip().splitlines())

pascalCortado=[]

for linhas in testandoPascal:
    aux=""
    for lt in linhas:
        #ehPonto=re.match(realPattern, lt)
        pascalCortado.append(lt.casefold()
        .replace('(',' ( ')
        .replace(')',' ) ')
        .replace("'"," ' ")
        .replace(',',' , ')
        .replace(';',' ;'))   
              
         
        #print(aux)
        

testandoPascal.clear()

for item in pascalCortado:
    testandoPascal.append(item.casefold().strip().split(' '))
    
    #.split(' '))

#for item in testandoPascal:
    #print(item)
    #for palavras in item:
       # print(palavras)
 
#essa impressão é importante!!
#print(testandoPascal)  
decVariavel=False
beginner=False
listaVariaveis=[]

abrestring=False



for itens in testandoPascal:
    if itens[0]=='begin':
        decVariavel=False   
    if decVariavel==True:
        listaVariaveis.append(itens[0])
        #print(itens) 
    for token in itens:
            if token in pascal_keys:
                lexemas.append([token, "key word"])
            elif token in pascal_datatype:
                lexemas.append([token, "datatype"])   
            elif token in pascal_operators:
                lexemas.append([token, "operator"])   
            elif token in pascal_separators:
                lexemas.append([token, "separator"])             
            elif re.match(integerPattern, token):
                lexemas.append([token, "integer"])
            elif re.match(realPattern, token):
                lexemas.append([token, "real"])
            elif token in listaVariaveis:
                lexemas.append([token, "variable"])
            elif token=='':
                continue
            else:
                lexemas.append([token, "unknow"])  
    if itens[0]=='var':
        decVariavel=True
                           
    


#print(pascal_code)
for woou in lexemas:
    print(woou)


#print(listaVariaveis)    

# with open("tokens.txt", "w") as lexemas_file:
# lexemas_file.write(str(lexemas))

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
