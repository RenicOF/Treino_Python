"""⚙️ Nível 2 – Intermediário (estrutura + lógica real)
🔹 Atividade 3: Mini sistema de cadastro
Crie um sistema que permita:
•	Cadastrar nomes em uma lista 
•	Listar todos os nomes 
•	Buscar um nome 
👉 Dica: usar while + menu	
"""


Lista_de_Cadastros = []

while True:
    Escolhar = input(
        "\nDigite:\n"
        "[1] Cadastrar nome\n"
        "[2] Listar nomes\n"
        "[3] Buscar nome\n"
        "[4] Remover nome\n"
        "[5] Sair\n"
        "Escolha: "
    )

    if Escolhar == "1":
        Nome = input("Qual nome você quer cadastrar: ")
        Lista_de_Cadastros.append(Nome)
        print("Nome cadastrado com sucesso!")

    elif Escolhar == "2":
        if len(Lista_de_Cadastros) == 0:
            print("Lista vazia!")
        else:
            for i, nome in enumerate(Lista_de_Cadastros):
                print(f"{i} - {nome}")

    elif Escolhar == "3":
        item = input("Digite o nome para buscar: ")
        if item in Lista_de_Cadastros:
            print(f"{item} está na lista no índice {Lista_de_Cadastros.index(item)}")
        else:
            print("Nome não encontrado!")

    elif Escolhar == "4":
        nome_r = input("Digite o nome que você quer remover: ")
        if nome_r in Lista_de_Cadastros:
            Lista_de_Cadastros.remove(nome_r)
            print("Removido com sucesso!")
        else:
            print("Nome não encontrado!")

    elif Escolhar == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Comando desconhecido")
    
