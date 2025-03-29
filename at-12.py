# Request the number of classes and total number of students from the user
number_of_classes = int(input("Enter the number of classes: "))
total_students = int(input("Enter the total number of students: "))

# Calculate the average number of students per class
average_students_per_class = total_students / number_of_classes

# Display the average number of students per class
print(f"A média de alunos por turma é: {average_students_per_class:.2f}")

# Check if any class has more than 40 students
if average_students_per_class > 40:
    print("Aviso: Algumas turmas têm mais de 40 alunos!")
