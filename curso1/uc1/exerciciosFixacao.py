#Exercicio 1
print("===EX 1===")
horas=int(input("Quantas horas?"))
valor=0

if horas<=0:
     print("Inválido")
elif horas<=2:
    valor=10
    print("Valor:",valor)
elif horas>2 and horas<=5:
    valor=20
    print("Valor:",valor)
else:
    valor=30
    print("Valor:",valor)

#Exercicio 2
print("===EX 2===")
nomePersonagem=str(input("Nome:"))
nivel=int(input("Nível:"))

print(nomePersonagem)
if nivel<1:
    print("Inválido")
elif nivel>=1 and nivel<=5:
    print("Aprendiz")
elif nivel>5 and nivel<16:
    print("Guerreiro")
elif nivel>15 and nivel<31:
    print("Veterano")
else:
 print("Lendário")   


#Exercicio 3
print("===EX 3===")
usuario_correto = "admin"
senha_correta = "python123"

usuario=input("Digite seu usuário:")
senha=input("Digite sua senha:")

if usuario==usuario_correto:
    if senha==senha_correta:
        print("Acesso autorizado")
    else:print("Senha incorreta")
else:print("Usuário incorreto")

#Exercicio 4
print("===EX 4===")
salarioMensal=float(input("Salário mensal:"))
valorSolicitado=float(input("Valor solicitado do empréstimo:"))
quantParcelas=int(input("Quantidade de parcelas:"))
valorParcela=valorSolicitado/quantParcelas

if salarioMensal<2000:
    print("Empréstimo negado, salário deve ser pelo menos 2000 reais")
elif valorSolicitado>salarioMensal*10:
    print("Empréstimo negado, valor solicitado acima de salário vezes 10")
elif valorParcela>salarioMensal*0.3:
    print("Empréstimo negado, o valor da parcela não pode ser acima de 30 do salário")
elif quantParcelas<1 or quantParcelas>48:
    print("Empréstimo negado, a quantidade de parcelas deve estar entre 1 e 48.")
else:
    print("Empréstimo aceito")

#Exercicio 5
print("===EX 5===")
nome = input("Digite o nome do personagem: ")
vida = float(input("Digite a vida atual do personagem: "))
ataque = float(input("Digite os pontos de ataque: "))
vida_inimigo = float(input("Digite a vida do inimigo: "))
defesa = float(input("Digite os pontos de defesa do inimigo: "))

dano = ataque - defesa

if vida <= 0:
    print( nome,"não pode atacar porque está sem vida.")
elif dano <= 0:
    print("O ataque não causou dano!")
else:
    vida_restante = max(0, vida_inimigo - dano)

    if dano >= vida_inimigo:
        print("O inimigo foi derrotado!")
    else:
        print("O inimigo sobreviveu.")
        print("Vida restante do inimigo:", vida_restante)


#Exercicio 6
print("===EX 6===")
idade = int(input("Digite sua idade: "))
aluno = input("É aluno matriculado? (sim/nao): ").lower()
autorizacao = input("Possui autorização do professor? (sim/nao): ").lower()
disponivel = input("O laboratório está disponível? (sim/nao): ").lower()

if disponivel == "sim" and idade >= 16 and (aluno == "sim" or autorizacao == "sim"):
    print("Acesso permitido!")
else:
    print("Acesso negado!")


#Exercicio 7
print("===EX 7===")
compra = float(input("Digite o valor da compra: R$ "))
regiao = input("Digite a região de entrega: ").lower()

if compra <= 0:
    print("Compra inválida.")
elif regiao != "sul" and regiao != "sudeste" and regiao != "centro-oeste" and regiao != "norte" and regiao != "nordeste":
    print("Região inválida.")
else:
    if compra >= 300:
        frete = 0
    elif regiao == "sul":
        frete = 15
    elif regiao == "sudeste":
        frete = 20
    elif regiao == "centro-oeste":
        frete = 25
    else:
        frete = 35

    total = compra + frete

    print("Valor da compra: R$", compra)
    print(f"Valor do frete: R$", frete)
    print(f"Valor total: R$", total) 



#Exercicio 8
print("===EX 8===")
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Triângulo inválido.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Triângulo inválido.")
elif a == b and b == c:
    print("Triângulo equilátero.")
elif a == b or a == c or b == c:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")