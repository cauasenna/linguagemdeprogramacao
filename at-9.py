# Request three numbers from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Find the largest and smallest number
largest = max(number1, number2, number3)
smallest = min(number1, number2, number3)

# Display the results
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
