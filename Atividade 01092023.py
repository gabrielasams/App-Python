print("Bem-vinde a Biblioteca de Gabriela")
print("_" * 34)

print("O que você deseja fazer? ")
print("_" * 34)

mangas = list()
livros = list()

while True:
                                        #Menu da Biblioteca
    print("""
        1 - Cadastro de livro
        2 - Cadastro de mangá
        3 - Visualização dos livros
        4 - Visualização dos mangás
        5 - Sair da Biblioteca 
        """)

    btn = int(input("Opção: "))

    if btn == 1:                                                #Cadastro de livro
        while True:

            nom: str = input("Nome do livro: ")
            gen: str = input("Gênero do livro: ")
            ano = int(input("Ano de lançamento: "))

            livro = {"nome": nom, "gen": gen, "ano": ano}
            livros.append(livro)

            pergunta0 = input("Deseja cadastrar mais um livro? Sim ou não. ").strip()[0].lower()
            if pergunta0 == "n":
                break

    if btn == 2:                                              #Cadastro de mangá
        while True:

            nome: str = input("Nome do mangá: ")
            gene: str = input("Gênero do mangá: ")
            anoo = int(input("Ano de lançamento: "))

            manga = {"nome": nome, "gen": gene, "ano": anoo}
            mangas.append(manga)

            pergunta1 = input("Deseja cadastrar mais um item? Sim ou não. ").strip()[0].lower()
            if pergunta1 == "n":
                break

    if btn == 3:                                                    #Lista de livros
        if len(livros):
            for livro in livros:

                for key, value in livro.items():
                  if key!= "nome":
                        print(f'{key.title()} : {value.title}')
                  else:
                        print(f'{key.title()} : {value.title}')
                        print("_" * 34)

    if btn == 4:                                                    #Lista de mangás
        if len(mangas):
            for manga in mangas:
                for key, value in manga.items():
                    if key != "nome":
                        print(f'{key.title()} : {value.title}')
                    else:
                        print(f'{key.title()} : {value.title}')
                        print("_" * 34)


    if btn == 5:
        print("Você saiu da Biblioteca.")
        break