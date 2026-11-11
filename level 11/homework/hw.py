
# 1.
# and - ორივე პირობა უნდა იყოს სწორი
# or - ერთი პირობა მაინც უნდა იყოს სწორი
# not - საპირისპირო შედეგს გვაძლევს

# 2.
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin123":
    print("Login successful!")
else:
    print("Login failed!")


# 3.
day = input("Enter day: ")

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a working day!")


# 4.
total = int(input("Enter total: "))

if total >= 100 and total < 500:
    print("You received a 10% discount!")
else:
    print("No discount available!")


# 5.
temperature = int(input("Enter temperature: "))

if temperature < 0 or temperature > 35:
    print("Extreme temperature!")
else:
    print("Temperature is normal!")


# 6.
number = int(input("Enter number: "))

if number % 3 == 0 or number % 5 == 0:
    print("Special number!")
else:
    print("Regular number!")


# 7.
# A. False
# B. True
# C. False
# D. True
# E. False

