seconds = int(input("Insira Um Valor Em Segundos"))

days = seconds // (24 * 3600)
seconds_remaining = seconds % (24 * 3600)

hours = seconds_remaining //  3600
seconds_remaining %= 3600

minutes = seconds_remaining // 60
final_seconds = seconds_remaining % 60

print(f"{seconds} segundos equivalem a:")
print(f"{days} dias, {hours} horas, {minutes} minutos e {final_seconds} segundos.")