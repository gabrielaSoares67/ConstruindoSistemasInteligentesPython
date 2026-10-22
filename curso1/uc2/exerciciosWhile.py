#Exercicio 1
""" numero=int(input("Digite um número: "))
contador=0

while contador<numero:
    contador+=1
    print(contador) """

#Exercicio 2
""" numero=int(input("Digite um número: "))
contador=numero + 1

while contador>0:
    contador-=1
    print(contador)  """

#Exercicio 3
""" numero=int(input("Digite um número: "))
contador=1

while contador<=10:
    resultado=contador*numero
    contador+=1
    print(resultado) """

#Exercicio 4
""" contador=0
soma=0
while contador<5:
    numero=int(input("Digite um número: "))
    soma+=numero
    contador+=1

print(soma) """

#Exercicio 5
""" alunos=int(input("Quantos alunos? "))
contador=0
media = 0
while contador<alunos:
    nota=float(input("Digite a nota: "))
    contador += 1
    media += nota
    mediaTurma = media / alunos

print(mediaTurma) """

#Exercicio 6
""" nota=float(input("Digite a nota: "))

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print("Nota registrada com sucesso!") """

#Exercicio 7
""" while True:
    print("\n=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1=int(input("Digite um número: "))
        num2=int(input("Digite um número: "))
        print("Soma:", num1+num2)

    elif opcao == "2":
        idade = int(input("Digite sua idade: "))
        if idade<18:
            print("Menor de idade")
        else:
            print("Maior de idade")

    elif opcao == "0":
        print("Encerrando")
        break

    else:
        print("Opção inválida") """

#Desafio 8
""" 
saldo = 500.00
depositos = 0
saques = 0

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Saldo atual: R$", saldo)

    elif opcao == "2":
        valor = float(input("Valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            depositos += 1
            print("Depósito realizado!")
        else:
            print("O valor deve ser maior que zero.")

    elif opcao == "3":
        valor = float(input("Valor do saque: R$ "))

        if valor <= 0:
            print("O valor deve ser maior que zero.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            saques += 1
            print("Saque realizado!")

    elif opcao == "0":
        print("\n=== RESUMO ===")
        print("Saldo final: R$", saldo)
        print("Depósitos realizados:", depositos)
        print("Saques realizados:", saques)
        
        break

    else:
        print("Opção inválida!")

 """