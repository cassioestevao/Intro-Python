print("Esse App é um verificador de nomes, favor preencher questionario!")
digite = str(input("qual é o seu nome? "))

if digite in "Ana Maria João Moises Lucas Carlos Mariana Edson Guilherme Lucas Pedro Gustavo Fabricio Julio Ronaldo Henrique Alexandre Douglas Mateus Ana Julia Larissa Vanessa":
    print("\033[32mOlá {}, O seu nome é muito popular!".format(digite))
elif digite in "Feio Magro Esquisito Não Nao sei Nada Indeferido":
    print("Seu nome é um nome comum ou indiferente! Estamos finalizando nossas pesquisas...")
    print("\033[31mOlá {}, O seu nome é muito diferente!".format(digite))
else:
    print("Seu nome é um nome comum ou indiferente! Estamos finalizando nossas pesquisas...")
    
