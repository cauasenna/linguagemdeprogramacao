import json
import os
from datetime import datetime

ARQUIVO = "usuarios.json"

# Carrega os dados do arquivo
def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return {}
    with open(ARQUIVO, "r") as f:
        return json.load(f)

# Salva os dados no arquivo
def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

# Criar um novo usuário
def criar_conta(usuarios):
    username = input("Novo nome de usuário: ")
    if username in usuarios:
        print("❌ Nome de usuário já existe.")
        return
    senha = input("Senha: ")
    usuarios[username] = {
        "senha": senha,
        "saldo": 0.0,
        "transacoes": []
    }
    salvar_usuarios(usuarios)
    print("✅ Conta criada com sucesso!")

# Fazer login
def login(usuarios):
    username = input("Nome de usuário: ")
    senha = input("Senha: ")
    if username in usuarios and usuarios[username]["senha"] == senha:
        print(f"✅ Login bem-sucedido! Bem-vindo(a), {username}")
        menu_banco(username, usuarios)
    else:
        print("❌ Usuário ou senha incorretos.")

# Registrar transação
def registrar_transacao(usuario, usuarios, tipo, valor):
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usuarios[usuario]["transacoes"].append({
        "tipo": tipo,
        "valor": valor,
        "data": data
    })

# Menu bancário após login
def menu_banco(usuario, usuarios):
    while True:
        print(f"\n--- Conta de {usuario} ---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver transações")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = usuarios[usuario]["saldo"]
            print(f"💰 Saldo atual: R${saldo:.2f}")
        elif opcao == "2":
            try:
                valor = float(input("Valor do depósito: "))
                if valor > 0:
                    usuarios[usuario]["saldo"] += valor
                    registrar_transacao(usuario, usuarios, "Depósito", valor)
                    salvar_usuarios(usuarios)
                    print("✅ Depósito realizado!")
                else:
                    print("❌ Valor inválido.")
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcao == "3":
            try:
                valor = float(input("Valor do saque: "))
                if 0 < valor <= usuarios[usuario]["saldo"]:
                    usuarios[usuario]["saldo"] -= valor
                    registrar_transacao(usuario, usuarios, "Saque", valor)
                    salvar_usuarios(usuarios)
                    print("✅ Saque realizado!")
                else:
                    print("❌ Valor inválido ou saldo insuficiente.")
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcao == "4":
            print("\n📜 Histórico de Transações:")
            transacoes = usuarios[usuario]["transacoes"]
            if not transacoes:
                print("Nenhuma transação registrada.")
            for t in transacoes:
                print(f"{t['data']} | {t['tipo']}: R${t['valor']:.2f}")
        elif opcao == "5":
            print("Saindo da conta...")
            break
        else:
            print("❌ Opção inválida.")

# Menu principal
def menu():
    usuarios = carregar_usuarios()

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Criar conta")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta(usuarios)
        elif opcao == "2":
            login(usuarios)
        elif opcao == "3":
            print("Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida.")

# Executar o sistema
menu()
