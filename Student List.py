"""
------------------------------------------------------------
Sistema de Gestão Escolar - Implementação Inicial

Estudante: Matheus Cesar de Lima
Curso: Análise e Desenvolvimento de Sistemas

Este sistema permite:
- Incluir estudantes (somente nome nesta etapa)
- Listar os estudantes cadastrados
- Exibir mensagens para funcionalidades ainda em desenvolvimento

Todas as informações são armazenadas em memória (lista).
------------------------------------------------------------
"""

# Lista para armazenar os nomes dos estudantes
estudantes = []

# Função principal para exibir o menu e controlar o fluxo do sistema
def exibir_menu_principal():
    while True:
        print("\nMENU PRINCIPAL - Sistema de Gestão Escolar")
        print("1. Operações com Estudantes")
        print("2. Listar Estudantes")
        print("3. Professores")
        print("4. Disciplinas")
        print("5. Turmas")
        print("6. Matrículas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_operacoes_estudante()  # Submenu de operações com estudante
        elif opcao == "2":
            listar_estudantes()
        elif opcao in ["3", "4", "5", "6"]:
            print("EM DESENVOLVIMENTO")
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Submenu de operações com estudante
def menu_operacoes_estudante():
    while True:
        print("\nMENU DE OPERAÇÕES DO ESTUDANTE")
        print("1. Incluir Estudante")
        print("2. Atualizar Estudante")
        print("3. Excluir Estudante")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            print("EM DESENVOLVIMENTO")
        elif opcao == "3":
            print("EM DESENVOLVIMENTO")
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Função para incluir um estudante
def incluir_estudante():
    nome = input("Digite o nome do estudante: ")
    if nome.strip():
        estudantes.append(nome.strip())
        print(f"Estudante '{nome}' cadastrado com sucesso.")
    else:
        print("Nome inválido. Tente novamente.")

# Função para listar estudantes
def listar_estudantes():
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        print("\nLista de Estudantes:")
        for i, nome in enumerate(estudantes, start=1):
            print(f"{i}. {nome}")

# Inicia o sistema
exibir_menu_principal()


