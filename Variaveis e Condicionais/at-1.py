school_grade1 = float(input())
school_grade2 = float(input())
school_grade3 = float(input())


arithmetic_mean = (school_grade1 + school_grade2 + school_grade3) / 3

print(f"Media Aritmetica Simples: {arithmetic_mean}")

weighted_average_a = (school_grade1 * 2 + school_grade2 * 2 + school_grade3 * 3) / (2 + 2 + 3)

print(f"Media Ponderada (Pesos 2, 2, 3): {weighted_average_a}")

weighted_average_b = (school_grade1 * 1 + school_grade2 * 2 + school_grade3 * 2 ) / (1 + 2 + 2)

print(f"Media Ponderada (Pesos 1, 2, 2): {weighted_average_b}")
