# EX 01
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro1 = Livro("Jantar secreto", "Raphael Montes", 362)
livro2 = Livro("A sete chaves", "Freida McFadden", 272)

print(livro1.titulo, livro1.autor, livro1.paginas)
print(livro2.titulo, livro2.autor, livro2.paginas)

livro1.paginas = 467

print(livro1.titulo, livro1.autor, livro1.paginas)
print(livro2.titulo, livro2.autor, livro2.paginas)


# EX 02 
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


retangulo1 = Retangulo(4, 3)
retangulo2 = Retangulo(5, 2)

print("Área 1:", retangulo1.calcular_area())
print("Área 2:", retangulo2.calcular_area())


# EX 03 
class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor = self.valor + 1

    def zerar(self):
        self.valor = 0


contador1 = Contador()
contador2 = Contador()

contador1.incrementar()
contador1.incrementar()
contador1.incrementar()

contador2.incrementar()

print(contador1.valor)
print(contador2.valor)

contador1.zerar()

print(contador1.valor)
print(contador2.valor)


# EX 04 
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def repor(self, quantidade):
        if quantidade <= 0:
            return False

        self.estoque = self.estoque + quantidade
        return True

    def vender(self, quantidade):
        if quantidade <= 0 or quantidade > self.estoque:
            return False

        self.estoque = self.estoque - quantidade
        return True

    def valor_em_estoque(self):
        return self.preco * self.estoque


produto = Produto("Caderno", 5.0, 4)

print(produto.vender(2))
print(produto.estoque)

print(produto.vender(3))
print(produto.estoque)

print(produto.repor(5))
print(produto.estoque)

print(produto.repor(0))
print(produto.estoque)

print(produto.valor_em_estoque())



# EX 05 
class LivroEmprestimo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return True
        else:
            return False


livro = LivroEmprestimo("Mil vezes amor")

print(livro.emprestar())
print(livro.emprestar())
print(livro.devolver())
print(livro.devolver())


# EX 06
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def quantidade_alunos(self):
        return len(self.alunos)


turma1 = Turma("Manhã")
turma2 = Turma("Noite")

turma1.matricular("Gabriela")
turma1.matricular("Nicolas")

turma2.matricular("Henrique")

print(turma1.nome, turma1.alunos)
print("Quantidade:", turma1.quantidade_alunos())

print(turma2.nome, turma2.alunos)
print("Quantidade:", turma2.quantidade_alunos())


# EX 07 
class ProdutoRelatorio:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def valor_em_estoque(self):
        return self.preco * self.estoque


produtos = [
    ProdutoRelatorio("Caderno", 10.0, 2),
    ProdutoRelatorio("Caneta", 3.0, 0),
    ProdutoRelatorio("Borracha", 2.0, 5)
]

total = 0
sem_estoque = 0

for produto in produtos:
    print(produto.nome)
    print(produto.estoque)
    print(produto.valor_em_estoque())

    total = total + produto.valor_em_estoque()

    if produto.estoque == 0:
        sem_estoque = sem_estoque + 1

print("Valor total:", total)
print("Sem estoque:", sem_estoque)


# EX 08
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor <= 0:
            return False

        self.saldo = self.saldo + valor
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False

        self.saldo = self.saldo - valor
        return True


conta1 = Conta("Gabriela")
conta2 = Conta("Guilherme")

print(conta1.depositar(50))
print(conta1.sacar(20))
print(conta1.sacar(40))
print(conta1.depositar(-10))

print("Saldo 1:", conta1.saldo)
print("Saldo 2:", conta2.saldo)



# EX 09 
class LivroBiblioteca:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return True
        else:
            return False


livros = [
    LivroBiblioteca("Os naturais"),
    LivroBiblioteca("O vilarejo"),
    LivroBiblioteca("Harry Potter")
]

while True:
    print("\n=== BIBLIOTECA ===")
    print("1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for livro in livros:
            if livro.emprestado == True:
                print(livro.titulo, "- Emprestado")
            else:
                print(livro.titulo, "- Disponível")

    elif opcao == "2":
        titulo = input("Digite o título: ")
        encontrado = False

        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True

                if livro.emprestar():
                    print("Empréstimo realizado!")
                else:
                    print("Livro já emprestado!")

                break

        if encontrado == False:
            print("Livro não encontrado")

    elif opcao == "3":
        titulo = input("Digite o título: ")
        encontrado = False

        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True

                if livro.devolver():
                    print("Devolução realizada!")
                else:
                    print("Livro não estava emprestado!")

                break

        if encontrado == False:
            print("Livro não encontrado")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")