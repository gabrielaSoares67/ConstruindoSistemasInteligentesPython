nomeAnalista = input("Nome ou apelido do analista: ")
identificacao = input("Identificação da mensagem: ")
grupos = int(input("Quantidade de grupos de símbolos: "))
tempoGrupo = float(input("Tempo por grupo, em minutos: "))


if grupos <= 0 or tempoGrupo <= 0:
    print("Dados inválidos")
else:
    total = grupos * tempoGrupo


    print("\n--- FICHA DA MENSAGEM ---")
    print("Analista:", nomeAnalista)
    print("Identificação:", identificacao)
    print("Quantidade de grupos:", grupos)
    print("Tempo total:", total, "minutos")


    if total <= 60:
        print("Análise dentro do prazo")
    else:
        print("Reorganizar o trabalho")
