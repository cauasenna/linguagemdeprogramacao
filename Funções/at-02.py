import json

ARQUIVO = "estoque.json"

# Carregar produtos do arquivo
def carregar_estoque():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Salvar produtos no arquivo
def salvar_estoque(produtos):
    with open(ARQUIVO, "w") as f:
        json.dump(produtos, f, indent=4)

# Adicionar novo produto
def adicionar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço unitário (R$): "))
    except ValueError:
        print("Quantidade e preço precisam ser números válidos.")
        return

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos = carregar_estoque()
    produtos.append(produto)
    salvar_estoque(produtos)
    print("Produto adicionado com sucesso!")

# Exibir produtos e valor total
def exibir_estoque():
    produtos = carregar_estoque()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    valor_total = 0
    print("\n--- Estoque Atual ---")
    for i, produto in enumerate(produtos, start=1):
        subtotal = produto["quantidade"] * produto["preco"]
        valor_total += subtotal
        print(f"{i}. {produto['nome']} | Qtd: {produto['quantidade']} | Preço: R${produto['preco']:.2f} | Subtotal: R${subtotal:.2f}")
    
    print(f"\n💰 Valor total do estoque: R${valor_total:.2f}")

# Menu principal
def menu():
    while True:
        print("\n--- Controle de Estoque ---")
        print("1. Adicionar produto")
        print("2. Exibir estoque")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_estoque()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
