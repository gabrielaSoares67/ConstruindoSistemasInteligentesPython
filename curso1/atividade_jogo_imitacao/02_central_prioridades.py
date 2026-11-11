identificacao = input("Identificação da mensagem: ")
disponivel = float(input("Tempo disponível, em minutos: "))
necessario = float(input("Tempo necessário, em minutos: "))
risco = input("A mensagem indica risco imediato? (sim/nao): ").lower()
pista = input("A mensagem contém uma pista recorrente? (sim/nao): ").lower()


if disponivel <= 0 or necessario <= 0:
    print("Tempo inválido")

elif (risco != "sim" and risco != "nao") or (pista != "sim" and pista != "nao"):
    print("Resposta inválida")

else:
    
    if necessario > disponivel:
        resultado = "Solicitar apoio: tempo insuficiente"
        print("Identificação:", identificacao)
        print("Resultado:", resultado)

    elif risco == "sim":
        resultado = "Prioridade máxima"
        restante = disponivel - necessario
        print("Identificação:", identificacao)
        print("Resultado:", resultado)
        print("Tempo restante:", restante, "minutos")

    elif pista == "sim":
        resultado = "Prioridade alta"
        restante = disponivel - necessario
        print("Identificação:", identificacao)
        print("Resultado:", resultado)
        print("Tempo restante:", restante, "minutos")

    else:
        resultado = "Prioridade normal"
        restante = disponivel - necessario
        print("Identificação:", identificacao)
        print("Resultado:", resultado)
        print("Tempo restante:", restante, "minutos")
