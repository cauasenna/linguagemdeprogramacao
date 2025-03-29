# Request the initial salary and the number of years from the user
initial_salary = float(input("Digite o salário inicial: "))
years = int(input("Digite o número de anos: "))

# Initialize the current salary as the initial salary
current_salary = initial_salary

# Loop through the years and apply the doubling percentage increase
for year in range(1, years + 1):
    # Double the percentage increase each year
    current_salary *= (1 + (0.1 * 2)**(year - 1))

# Display the current salary after the specified number of years
print(f"O salário após {years} anos é: {current_salary:.2f}")
