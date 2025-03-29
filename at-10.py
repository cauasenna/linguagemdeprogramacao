# Request an integer greater than 1
number = int(input("Enter an integer greater than 1: "))

# Check if the number is greater than 1
if number <= 1:
    print("The number must be greater than 1.")
else:
    # Check if the number is prime
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    
    # Display if the number is prime or not
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
