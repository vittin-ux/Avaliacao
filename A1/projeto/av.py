print("=== Sistema de Gerenciamento de Alunos ===")

alunos = []  # lista de dicionários

while True:
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota a um aluno")
    print("3 - Listar alunos")
    print("4 - Exibir alunos com notas")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        alunos.append({"nome": nome, "notas": []})
        print("Aluno cadastrado!")

    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")
        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == nome.lower():
                nota = float(input("Digite a nota: "))
                aluno["notas"].append(nota)
                encontrado = True
                print("Nota adicionada!")
                break

        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "3":
        print("\n=== Alunos Cadastrados ===")
        for aluno in alunos:
            print(f"- {aluno['nome']}")

    elif opcao == "4":
        print("\n=== Alunos e Suas Notas ===")
        for aluno in alunos:
            notas = aluno["notas"]
            media = sum(notas) / len(notas) if notas else 0
            print(f"{aluno['nome']} - Notas: {notas} | Média: {media:.2f}")

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")