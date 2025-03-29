# Request username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username and password are the same
if username == password:
    print("Error: Username and password cannot be the same.")
else:
    print("Login successful!")
