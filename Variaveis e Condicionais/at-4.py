car_rental = int(input("insira por quantos dias voçê vai alugar o carro:"))
kilometers_driven = float(input("Insira a quantidade de quilometros que foram rodados:"))

fixed_cost = car_rental * 90

if kilometers_driven <= 100:
    extra_fee = 0 
else:
    surplus = kilometers_driven - 100
    extra_fee = surplus * 12

total_amount = fixed_cost + extra_fee

print(f"O valor total a ser pago pelo aluguel do carro é: R${total_amount}")