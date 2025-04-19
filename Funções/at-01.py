import json
from datetime import datetime

ARQUIVO = "tarefas.json"

# Carregar tarefas do arquivo
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Salvar tarefas no arquivo
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

# Adicionar nova tarefa
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    prazo = input("Digite o prazo (AAAA-MM-DD): ")
    
    tarefa = {
        "descricao": descricao,
        "prazo": prazo,
        "concluida": False
    }
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

# Listar tarefas
def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas.sort(key=lambda x: x["prazo"])  # Ordena por data
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {tarefa['descricao']} | Prazo: {tarefa['prazo']} | Status: {status}")

# Marcar tarefa como concluída
def concluir_tarefa():
    listar_tarefas()
    tarefas = carregar_tarefas()
    try:
        indice = int(input("\nDigite o número da tarefa que deseja concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Menu principal
def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
