""" #Exercicio 1-peça o nome, a cidade e a idade da pessoa. Mostre uma ficha e calcule quantos anos ela terá no próximo aniversário
print("===Ex 1===")
nome=input("Qual seu nome?")
cidade=input("Qual sua cidade?")
idade=int(input("Qual sua idade?"))
print("===FICHA===\nNome:",nome,"\nCidade:",cidade,"\nIdade:",idade,"\nNo próximo ano terá:",idade+1)


#Exercicio 2-Leia o preço de um lanche e a quantidade comprada. Calcule o total. Considere preço e quantidade positivos. Se o total for a partir de R$ 50,00, aplique 10% de desconto; caso contrário, mantenha o valor original. Mostre o total antes do desconto, o desconto e o valor final. Para calcular 10%, multiplicar o total por 0.10. Teste totais abaixo de 50, iguais a 50 e acima de 50.
print("===Ex 2===")
preco=float(input("Qual o preço?"))
quantidade=int(input("Quantidade comprada?"))
total= preco*quantidade
desconto=0
total2=0

if total >= 50:
    total2= total*0.9
    desconto=total*0.1

print("Preço:", total,"Desconto:",desconto,"Preço com desconto:",total2)


#Exercicio3- Leia dois números inteiros. Informe se o primeiro é maior, se o segundo é maior ou se os dois são iguais. Use uma cadeia if// elif.else
print("===Ex 3===")
num1=int(input("Digite um valor inteiro:"))
num2=int(input("Digite um valor inteiro:"))

if num1>num2:
    print("O primeiro valor é maior.")
elif num2>num1:
    print("O segundo valor é maior.")
else:
    print("Os dois são iguais.") """


#Exercicio4- Leia uma temperatura e mostre apenas uma classificação:abaixo de 18: Ambiente frio;
""" a partir de 18 e abaixo de 26: Ambiente agradável;
a partir de 26: Ambiente quente.
Teste especialmente os valores 18e 26. """
""" print("===Ex 4===")
temperatura=int(input("Digite uma temperatura:"))
if temperatura<18:
    print("Ambiente frio.")
elif 18>=temperatura and temperatura <26:
    print("Ambiente agradavel.")
else:
    print("Ambiente quente.") """



  #Exercicio 5- Leia duas notas do mesmo peso. Se alguma nota estiver fora da faixa de 0 a 10, mostre Nota inválidae não calcule a média. Caso ambas sejam válidas, calcule e mostre a média e a situação:
"""média a partir de 7: aprovado;
média a partir de 5 e abaixo de 7: recuperação;
média abaixo de 5: reprovado. """
# print("===Ex 5===")
# nota1=float(input("Digite uma nota:"))
# nota2=float(input("Digite uma nota:"))
# media=(nota1+nota2)/2
# if nota1 >=0 and nota1 <= 10 and nota2 >=0 and nota2 <= 10:
#     if media >= 7:
#         print("Aprovado")
#     elif media >=5 and media <= 7:
#         print("Recuperação")
#     else:
#         print("Reprovado")
# else:
#     print("Nota inválida")

#Leia a idade e pergunte se a pessoa possui inscrição ( sim/nao). Considere idade não negativa e uma das duas respostas indicadas. A entrada só será permitida para quem tiver pelo menos 14 anos e inscrição confirmada.Usar and. Teste uma pessoa que atenda a dois critérios, outra que atenda a apenas um e outra que não atenda a nenhum.
# print("===Ex 6===")
# idade6=int(input("Qual a idade?"))
# possuiInscricao=input("Possui inscrição?(sim/nao)").lower()

# if idade>=0:
#     if idade>=14 and possuiInscricao in "sim":
#         print("Entrada permitida")
# else:
#         print("Entrada não permitida")


#ex 7-Leia uma idade não negativa. Neste museu fictício, pessoas com menos de 12 anos ou a partir de 60 anos têm entrada gratuita. As demais pagam R$ 20,00. Use or e teste como idades 11, 12, 59e 60.
# print("===Ex 7===")
# idade7=int(input("digite idade:"))
# if idade7>=0:
#     if 12<=idade7 or idade7>=60:
#         print("Entrada gratuita")
#     else:
#         print("Entrada 20 reais")


#ex 8-A biblioteca tem 8 exemplares disponíveis. Leia a quantidade que uma pessoa deseja retirar.
# Se a quantidade for menor ou igual a zero, informe que o pedido é inválido.
# Se for maior que o estoque, informe que não há exemplares suficientes.
# Caso contrário, confirme o pedido, atualize o estoque e mostre a quantidade restante.
# O estoque só deve diminuir quando o pedido for confirmado.
# print("===Ex 8===")
# disponiveis=8
# quantP=int(input("Quantidade de pessoas:"))
# if quantP<=0:
#     print("Invalido")
#     if quantP>disponiveis:
#         print("não há exemplares suficientes")
#     else:
#         print("Pedido confirmado.")
#         disponiveis-=quantP
#         print("Restantes:", disponiveis)


#Exercício 9
""" num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("===== CALCULADORA =====\nDigite a operação que deseja:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
operacao = int(input("Qual a operação deseja fazer? "))

if operacao >= 1 and operacao <= 4:
    if operacao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacao == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Opção Inválida") """

#Exercício 10
""" idade = int(input("Idade: "))
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao == "sim":
    print("Participação permitida.")
else:
    print("Participação não permitida.") """

#Desafio Extra