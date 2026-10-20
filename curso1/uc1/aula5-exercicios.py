#Exercicio 12
print("===Contas===")
print("12 + 3")
print(12 + 3)
print("Resultado:", 12 + 3)
print("12", "3")
#a primeira é String, entao o calculo não é feito, só imprime o que esta entre aspas, o segundo faz a conta

#Exercicio 13
nome= "Robótica para iniciantes"
sala= "Laboratório 2"
vagas=24
duracaoHoras= 2.5
inscricoesAbertas=True

print("===AULA===", "\nNome:", nome," Tipo:",type(nome), "\nSala:", sala, "Tipo:", type(sala), "\nVagas:",vagas,"Tipo:", type(vagas),"\n Duracao em horas",duracaoHoras,"Tipo:",type(duracaoHoras),"\nInscricoes abertas:", inscricoesAbertas,"Tipo:",type(inscricoesAbertas))
#String: é todo o texto em aspas, nome e sala
#Int sao numeros inteiros, vagas
#Float: numeros decimais, duracaoemHoras
#Bool: ttrue or false, inscricoesAbertas

#Exercicio 14
print("===PIZZA===")
precoPizza=48.00
precoBebida=12.00
quantAmigos=4
totalSoma=precoBebida+precoPizza
totalPessoa=totalSoma/4

print("Total:", totalSoma,"\nTotal por pessoa:",totalPessoa,type(totalPessoa))

#Exercicio 15
print("===BIBLIOTECA===")
livrosDisponiveis=40
print("Total de livros disponiveis:", livrosDisponiveis)
livrosDisponiveis+=12
print("Total de livros disponiveis,  com mais 12:", livrosDisponiveis)
livrosDisponiveis-=9
print("Total de livros disponiveis, com 9 emprestados:", livrosDisponiveis)
livrosDisponiveis+=4
print("Total de livros disponiveis, com 4 devolucoes:", livrosDisponiveis)
livrosDisponiveis-=6
print("Total de livros disponiveis, com mais 6 emprestados:", livrosDisponiveis)

#Exercicio 16
print("===BOLETIM===")
nomeAluno="Guilherme"
nota1=7.5
nota2=8.0
nota3=9.5
somaNotas=nota1+nota2+nota3
mediaNotas= somaNotas/3

print("Nome:", nomeAluno, "\nNota 1:", nota1,"\nNota 2:", nota2,"\nNota 3:", nota3, "\nMédia:", mediaNotas)

nota2=6.5
somaNotas=nota1+nota2+nota3
mediaNotas= somaNotas/3

print("Nome:", nomeAluno, "\nNota 1:", nota1,"\nNota 2:", nota2,"\nNota 3:", nota3, "\nMédia:", mediaNotas)

#Exercicio 17
print("===CORRECAO===")
nomeCurso = "Python básico"#nome variavel sem espaco
mensalidade = 89.90#ponto ao inves de virgula
matricula_ativa = True#letra inicial maiuscula

print("Curso:", nomeCurso)
print("Mensalidade:", mensalidade)#variavel com letra minuscula
print("Matrícula ativa:", matricula_ativa)

print(type(mensalidade))

#Exercicio 18
print("===SALDO===")
saldo = 80
saldo_anterior = saldo 

saldo = saldo - 25 
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior)#80
print("Saldo atual:", saldo)#65
saldo+=15
print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)


#Exercicio 19
print("===PASSEIO===")
numAlunos=20
valorIngresso=15.00
valorLanche=10.00
custoOnibus=600.00
totalIngressos=valorIngresso*numAlunos
totalLanche=numAlunos*valorLanche
totalPasseio=totalIngressos+totalLanche+custoOnibus
custoPorAluno=totalPasseio/numAlunos

print("Total de alunos:", numAlunos,"\nCusto onibus:", custoOnibus, "\nValor Ingresso:", valorIngresso, "\nValor lanche:", valorLanche, "\nValor total do passeio:",totalPasseio,"\n Cada aluno devera pagar:", custoPorAluno)
numAlunos=25
totalIngressos=valorIngresso*numAlunos
totalLanche=numAlunos*valorLanche
totalPasseio=totalIngressos+totalLanche+custoOnibus
custoPorAluno=totalPasseio/numAlunos
print("Total de alunos:", numAlunos,"\nCusto onibus:", custoOnibus, "\nValor Ingresso:", valorIngresso, "\nValor lanche:", valorLanche, "\nValor total do passeio:",totalPasseio,"\n Cada aluno devera pagar:", custoPorAluno)


#Exercicio 21
print("===DESAFIO===")

nome = "Atlas"
energia = 100
distancia_percorrida = 0
amostras_coletadas = 0
missao_em_andamento = True

print("===== FICHA INICIAL DO ROBÔ =====")
print(f"Nome: {nome}")
print(f"Energia: {energia} pontos")
print(f"Distância percorrida: {distancia_percorrida} metros")
print(f"Amostras coletadas: {amostras_coletadas}")
print(f"Missão em andamento: {missao_em_andamento}")
print()


distancia_percorrida += 120
energia -= 20

print("1. O robô percorreu 120 metros.")
print(f"Distância total: {distancia_percorrida} metros")
print(f"Energia restante: {energia} pontos")
print()


amostras_coletadas += 3
energia -= 15

print("2. O robô coletou 3 amostras.")
print(f"Total de amostras: {amostras_coletadas}")
print(f"Energia restante: {energia} pontos")
print()


energia += 10

print("3. O robô recarregou a bateria.")
print(f"Energia atual: {energia} pontos")
print()


distancia_percorrida += 80
energia -= 25

print("4. O robô percorreu mais 80 metros.")
print(f"Distância total: {distancia_percorrida} metros")
print(f"Energia restante: {energia} pontos")
print()


amostras_coletadas += 2
energia -= 10

print("5. O robô coletou mais 2 amostras.")
print(f"Total de amostras: {amostras_coletadas}")
print(f"Energia restante: {energia} pontos")
print()


missao_em_andamento = False

print("6. A missão foi encerrada.")
print(f"Missão em andamento: {missao_em_andamento}")
print()


print("===== FICHA FINAL DO ROBÔ =====")
print(f"Nome: {nome}")
print(f"Energia restante: {energia} pontos")
print(f"Distância total percorrida: {distancia_percorrida} metros")
print(f"Amostras coletadas: {amostras_coletadas}")
print(f"Missão em andamento: {missao_em_andamento}")
print()

# Parte extra: distância média por minuto
duracao_missao = 4
distancia_media = distancia_percorrida / duracao_missao

print("===== DESEMPENHO DA MISSÃO =====")
print(f"Duração da missão: {duracao_missao} minutos")
print(f"Distância média: {distancia_media} metros por minuto")

