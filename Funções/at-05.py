import json
import os

ARQUIVO = "contatos.json"

# Carregar contatos do arquivo
def carregar_contatos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

# Salvar contatos no arquivo
def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f, indent=4)

# Adicionar novo contato
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos = carregar_contatos()
    contatos.append(contato)
    salvar_contatos(contatos)
    print("✅ Contato adicionado com sucesso!")

# Buscar contato por nome
def buscar_contato():
    nome_busca = input("Digite o nome para buscar: ").lower()
    contatos = carregar_contatos()
    encontrados = [c for c in contatos if nome_busca in c["nome"].lower()]

    if encontrados:
        print("\n📇 Contatos encontrados:")
        for i, c in enumerate(encontrados, start=1):
            print(f"{i}. Nome: {c['nome']} | Telefone: {c['telefone']} | Email: {c['email']}")
    else:
        print("❌ Nenhum contato encontrado.")

# Menu principal
def menu():
    while True:
        print("\n--- Gerenciador de Contatos ---")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            buscar_contato()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# Iniciar sistema
menu()
