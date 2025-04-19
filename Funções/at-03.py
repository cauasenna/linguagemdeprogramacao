import json

ARQUIVO = "assentos.json"
LINHAS = 5
COLUNAS = 5

# Carrega os assentos do arquivo ou cria um novo mapa
def carregar_assentos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [["L" for _ in range(COLUNAS)] for _ in range(LINHAS)]

# Salva os assentos no arquivo
def salvar_assentos(assentos):
    with open(ARQUIVO, "w") as f:
        json.dump(assentos, f)

# Mostra o mapa de assentos
def exibir_mapa(assentos):
    print("\nMapa de Assentos (L = Livre, X = Ocupado):\n")
    print("   " + " ".join([f"{c+1}" for c in range(COLUNAS)]))
    for i, linha in enumerate(assentos):
        print(f"{chr(65+i)}  " + " ".join(linha))

# Reservar um assento (ex: A1, C3)
def reservar_assento(assentos):
    exibir_mapa(assentos)
    codigo = input("\nDigite o código do assento que deseja reservar (ex: B2): ").upper()

    try:
        linha = ord(codigo[0]) - 65
        coluna = int(codigo[1:]) - 1

        if assentos[linha][coluna] == "X":
            print("❌ Assento já está reservado.")
        else:
            assentos[linha][coluna] = "X"
            salvar_assentos(assentos)
            print("✅ Assento reservado com sucesso!")

    except (IndexError, ValueError):
        print("❌ Código inválido.")

# Cancelar uma reserva
def cancelar_reserva(assentos):
    exibir_mapa(assentos)
