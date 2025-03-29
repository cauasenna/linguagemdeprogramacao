def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Lista para armazenar os números primos encontrados
primos = []
numero = 2  # Começamos a verificação a partir do 2

# Enquanto ainda não tivermos 100 primos, continuamos procurando
while len(primos) < 100:
    if eh_primo(numero):
        primos.append(numero)  # Adiciona o número primo à lista
    numero += 1  # Passa para o próximo número

# Exibir os 100 primeiros números primos
print(primos)
