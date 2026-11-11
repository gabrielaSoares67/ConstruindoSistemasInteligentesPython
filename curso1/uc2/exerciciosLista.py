#Ex1
""" objetos = ["celular", "mesa", "cadeira", "livro", "caneta"]

print("Lista completa:", objetos)
print("Quantidade:", len(objetos))
print("Primeiro objeto:", objetos[0])
print("Último objeto:", objetos[-1])

objetos[2] = "computador"

print("Lista atualizada:", objetos) """

#Ex2
""" colegas = []

for i in range(4):
    nome = input("Digite um nome: ")
    colegas.append(nome)

print("Nomes cadastrados:")

for nome in colegas:
    print(nome) """

#Ex3
""" numeros = []

for i in range(6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Lista:", numeros)
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))
print("Maior:", max(numeros))
print("Menor:", min(numeros)) """


#Ex4
""" mochila = ["corda", "água", "mapa", "água"]

item = input("Digite o item que deseja procurar: ").lower()

if item in mochila:
    print("O item existe na mochila.")
else:
    print("O item não existe na mochila.")

print("Quantidade de vezes:", mochila.count(item)) """

#Ex5
numeros = []
pares = []

for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Lista original:", numeros)
print("Números pares:", pares)