# Varavies escalares
# Lista - Vetor
# Lista de Listas - Matriz
# Texto - String

# Dict - dicionário - JSON!

info = { "name": "Maria José", "id": 1000, "codes":[20,30,44,50,60,66], \
         "vals":{"val":1000.88,"bal":500.00,"qtd": 400}}

sub = info["vals"]

print(info["name"])
print(info["codes"])
print(info["codes"][4])# O '-1' retorna o último item da lista

print(sub)
print(sub.keys())
print(sub.values())