#Ex1
""" limite = int(input("Digite um número inteiro positivo: "))

if limite > 0:
    for numero in range(1, limite + 1):
        print(numero)
else:
    print("Valor inválido!") """

#Ex2
""" numero = int(input("Digite um número maior ou igual a zero: "))

if numero >= 0:
    for n in range(numero, -1, -1):
        print(n)

    print("Lançamento realizado!")
else:
    print("Valor inválido!") """

#Ex3
""" limite = int(input("Digite um número inteiro positivo: "))

if limite <= 0:
    print("Limite inválido!")
elif limite == 1:
    print("Não há pares no intervalo.")
else:
    for numero in range(2, limite + 1, 2):
        print(numero) """

#Ex4
""" numero = int(input("Digite um número inteiro: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado) """

#Ex5
""" soma = 0
positivos = 0

for i in range(1, 7):
    numero = int(input("Digite um número inteiro: "))

    soma += numero

    if numero > 0:
        positivos += 1

print("Soma:", soma)
print("Quantidade de positivos:", positivos) """

#Ex6
""" quantidade = int(input("Quantos alunos há na turma? "))

if quantidade <= 0:
    print("Quantidade inválida!")
else:
    soma = 0
    aprovados = 0

    for aluno in range(1, quantidade + 1):
        nota = float(input("Digite a nota do aluno: "))

        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida. Digite novamente: "))

        soma += nota

        if nota >= 7:
            aprovados += 1

    media = soma / quantidade

    print("Média da turma:", media)
    print("Alunos com nota a partir de 7:", aprovados) """

#Ex7
""" palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

contador = 0

for caractere in palavra:
    if caractere == letra:
        contador += 1

print("Quantidade de vezes:", contador) """


#Ex8
""" codigo_correto = "ROBO123"
acertou = False

for tentativa in range(1, 4):
    print("Tentativa:", tentativa)
    codigo = input("Digite o código: ")

    if codigo == codigo_correto:
        acertou = True
        break
    else:
        print("Código incorreto!")

if acertou:
    print("Acesso autorizado!")
else:
    print("As tentativas acabaram!") """

#Desafio
""" energia = 100
soma_pontos = 0
missoes_realizadas = 0

for missao in range(1, 6):
    if energia < 25:
        print("Energia insuficiente")
        break

    print("Missão:", missao)

    pontuacao = int(input("Digite a pontuação (0 a 100): "))

    while pontuacao < 0 or pontuacao > 100:
        pontuacao = int(input("Pontuação inválida. Digite novamente: "))

    energia -= 25
    soma_pontos += pontuacao
    missoes_realizadas += 1

print("Missões realizadas:", missoes_realizadas)
print("Pontuação total:", soma_pontos)

if missoes_realizadas > 0:
    media = soma_pontos / missoes_realizadas
    print("Média de pontos:", media)

print("Energia restante:", energia) """