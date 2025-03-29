# Request an odd number from the user
number = int(input("Enter an odd number: "))

# Check if the number provided is odd
if number % 2 == 0:
    print("The number entered is not odd. Please enter an odd number.")
else:
    # Calculate the previous and next odd numbers
    previous = number - 2
    next_odd = number + 2

    # Calculate the squares of the numbers
    square_previous = previous ** 2
    square_next = next_odd ** 2

    # Calculate the difference between the squares
    difference = square_next - square_previous

    # Display the result
    print(f"The difference between the square of the next odd number ({square_next}) and the square of the previous number ({square_previous}) is: {difference}")
