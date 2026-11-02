# 1. კომენტარი: როდის და როგორ მუშაობს if-else
# if ამოწმებს მოცემულ პირობას თუ პირობა ჭეშმარიტია (True), სრულდება if ბლოკის კოდი.
# თუ პირობა მცდარია (False), პროგრამა გადადის else ბლოკზე და ასრულებს მის კოდს.


# 2. რიცხვის ლუწობა/კენტობის შემოწმება
number = int(input("შეიყვანეთ რიცხვი: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 3. ფასდაკლების შემოწმება (10%-იანი ფასდაკლება 100-ზე მეტზე)
total_amount = float(input("სრული გადასახადი: "))
if total_amount > 100:
    discounted_price = total_amount * 0.9
    print(f"ფასდაკლებული თანხა: {discounted_price}")
else:
    print("No discount!")


# 4. ტემპერატურის შემოწმება
temperature = float(input("შეიყვანეთ ტემპერატურა: "))
if temperature > 25:
    print("It's hot outside!")
else:
    print("It's not hot outside!")


# 5. ორი რიცხვის შედარება
num1 = float(input("პირველი რიცხვი: "))
num2 = float(input("მეორე რიცხვი: "))

if num1 > num2:
    print(f"პირველი რიცხვი {num1} უფრო დიდია.")
elif num2 > num1:
    print(f"მეორე რიცხვი {num2} უფრო დიდია.")
else:
    print("ორივე რიცხვი ტოლია.")




    