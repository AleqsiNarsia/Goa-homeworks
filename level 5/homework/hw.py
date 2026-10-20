#დავალება ნომერი 1

name = input("your name: ")
surname = input("your surname: ")
age = input("your age: ")
print(f"hello, my name is {name} {surname} i am {age} years old")


#დავალება ნომერი 2

product_1 = float(input("price: "))
product_2 = float(input("price: "))
product_3 = float(input("price: "))
total = product_1 + product_2 + product_3
print(f"total: {total}")


#დავალება ნომერი 3

current_age = int(input("your age: "))
years = int(input("years: "))

future_age = current_age + years

print(f"in {years} years you will be {future_age} years old")


#დავალება ნომერი 4

distance = float(input("მანძილი (კმ): "))
time = float(input("შეიყვანეთ დახარჯული დრო: "))

average_speed = distance / time

print(f"საშვალო სიჩქარე: {average_speed} კმ/სთ")


#დავალება ნომერი 5


distance = float(input("შეიყვანეთ გასავლელი მანძილი (კმ): "))
fuel_needed = (distance * 8) / 100

print(f"სულ დასჭირდება: {fuel_needed} ლიტრი საწვავი")


#დავალება ნომერი 6

distance = float(input("შეიყვანეთ გასავლელი მანძილი (კმ): "))
fuel_consumption = float(input("შეიყვანეთ საწვავის ხარჯი ყოველ 100კმ-ზე: "))
fuel_price = float(input("შეიყვანეთ 1 ლიტრი საწვავის ფასი ლარებში: "))

total_fuel = (distance * fuel_consumption) / 100

total_cost = total_fuel * fuel_price

print(f"დახარჯული საწვავი: {total_fuel} ლიტრი")
print(f"სულ დასახარჯი თანხა: {total_cost}₾")


#დავალება ნომერი 7

hourly_wage = float(input("შეიყვანეთ საათობრივი ანაზღაურება (ლარი): "))
hours_worked = float(input("შეიყვანეთ კვირის განმავლობაში ნამუშევარი საათები: "))

weekly_salary = hourly_wage * hours_worked

print(f"ერთი კვირის ხელფასი: {weekly_salary}₾")


#დავალება ნომერი 8

total_amount = float(input("შეიყვანეთ თანხის რაოდენობა (ლარი): "))
people_count = int(input("შეიყვანეთ ადამიანების რაოდენობა: "))


per_person = total_amount // people_count

remainder = total_amount % people_count

print(f"თითოეულ ადამიანს შეხვდება: {per_person}₾")
print(f"ნაშთად დარჩება: {remainder}₾")


#დავალება ნომერი 9

initial_price = float(input("შეიყვანეთ პროდუქტების საწყისი ფასი: "))
discount_percent = float(input("შეიყვანეთ ფასდაკლების პროცენტი (%): "))

discount_amount = (initial_price * discount_percent) / 100

final_price = initial_price - discount_amount

print(f"ფასდაკლების თანხა: {discount_amount}₾")
print(f"საბოლოო ფასი: {final_price}₾")


#დავალება ნომერი 10

total_pages = int(input("შეიყვანეთ წიგნის გვერდების რაოდენობა: "))
pages_per_day = int(input("რამდენ გვერდს კითხულობს ერთ დღეში: "))

import math
days_needed = math.ceil(total_pages / pages_per_day)

print(f"წიგნის წასაკითხად დასჭირდება: {days_needed} დღე")





