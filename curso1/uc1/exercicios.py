#Exercicio 1
nome= "Gabriela"
cidade= "Sapucaia do Sul"
idade= 16
tecnologia="Java"

print("=========MEU PERFIL=========")
print("Nome:",nome,"\nCidade:",cidade,"\nIdade:",idade,"\nTecnologia:",tecnologia)

#Exercicio 2
print("=========PRODUTO=========")
nome="Celular"
preço="5000"
quantidadeEmEstoque=100
disponível=True

print("Produto:", nome,"\nPreço:",preço,"\nQuantidade em estoque:", quantidadeEmEstoque, "\nDisponível:",disponível)


#Exercicio 3
print("=========PONTOS=========")
pontos = 250
pontos += 120
pontos -= 50
pontos += 30

print("Pontuação final:", pontos)

#Exercicio 4
print("=========COMPRA=========")
preco=18.50
quantidade=4
total=18.50*4

print("Valor da compra:",total)

#Exercicio 5
print("=========CONVERSAO=========")
horas=7
print(horas,"horas equivalem a", horas*60,"minutos.")

#Exercicio 6
print("=========VIDA=========")
vida=200
vida = 200
vida -= 45
vida -= 30
vida += 20
print("Quantidade final de vida:",vida)

#Exercicio 7
print("=========SALARIO=========")
salario=2800
bonus=450
salarioFinal=salario+bonus
print("Salário final:", salario)

#Exercicio 8
print("=========AREA=========")
largura=10
altura=20
area=largura*altura
print("Área:", area)

#Exercicio 9
print("=========TIPOS=========")
titulo = "Python"#string
versao = 3#int
nota = 9.5#float
finalizado = False#boolean
print(type(titulo))
print(type(versao))
print(type(nota))
print(type(finalizado))

#Exercicio 10
nome="Harry"
classe="Bruxo"
nivel=20
vida=100
ataque=20
defesa=10
possuiMagia=False

poderTotal=ataque+defesa

print("========================\nPERSONAGEM\n========================")
print("Nome:", nome,"\nClasse:",classe,"\nNível:",nivel,"\nVida:",vida,"\nAtaque:",ataque,"\nDefesa:", defesa,"\nPoder total:", poderTotal,"\nPossui magia?",possuiMagia)

#Exercicio bonus
print("=========PERSONAGEM 2=========")
nome="Nicolas"
vida=100
ouro=100
nivel=10

ouro+=20
vida-=10
ouro-=15
vida+=10
nivel+=1

print("Nome:",nome,"\nVida:",vida,"\nOuro:",ouro,"\nNível:",nivel)