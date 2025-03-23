product = float(input("Insira O Valor Da Mercadoria: "))

if product < 500:
    tax = 0
else:
    value_that_exceeds = product - 500
    tax = 0.5 * value_that_exceeds

final_value = product + tax
    

print(f"Valor das mercadorias: R$ {product}")
print(f"Imposto calculado: R$ {tax}")
print(f"Valor final a ser pago: R$ {final_value}")