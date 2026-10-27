# 1. input() - გვაძლევს საშვალებას მომხმარებელს შემოვაყვანინოთ რაიმე ტექსტი ან რიცხვი მაგ:name = input("სახელი: "),age = input("ასაკი: ")
# 2. Type Casting - მონაცემთა ტიპის შეცვლა (მაგ: int(), str())
# 3. ტიპები: str ("ტექსტი"), int (10), float (3.14), bool (True/False)
# 4. შედარებები: == (ტოლია), != (არ არის ტოლი), > (მეტია), < (ნაკლებია), >= (მეტია/ტოლია), <= (ნაკლებია/ტოლია)


#5
n1 = float(input("რიცხვი 1: "))
n2 = float(input("რიცხვი 2: "))
print(n1==n2, n1!=n2, n1>n2, n1<n2, n1>=n2, n1<=n2)


#6
age = int(input("შეიყვანეთ ასაკი: "))
check = age >= 18
print(check)


#7
s = float(input("სიჩქარე: ")) 
d = float(input("მანძილი: "))
t = float(input("დრო: "))
required_time = d / s
print(f"საჭირო დრო: {required_time}სთ | ჩაეტევა: {required_time <= t}")


#8
p1 = float(input("1-ის ფასი: "))
p2 = float(input("2-ის ფასი: "))
p3 = float(input("3-ის ფასი: "))
my_money = float(input("შენი თანხის რაოდენობა?: "))

total_price = p1 + p2 + p3
is_enough = my_money >= total_price
print("ეყოფა თუ არა თანხა?", is_enough)


#9
program_size = float(input("პროგრამის ზომა (GB): "))
free_space = float(input("თავისუფალი ადგილი კომპიუტერში (GB): "))

has_space = free_space >= program_size
print("ეყოფა თუ არა თავისუფალი მეხსიერება", has_space)


#10
math = float(input("მათემატიკის წლიური ნიშანი: "))
history = float(input("ისტორიის წლიური ნიშანი: "))
art = float(input("ხატვის წლიური ნიშანი: "))

average = (math + history + art) / 3
exceeds_five = average > 5
will_get_punished = average < 5 #5 ზე დაბალს თუ მიიღებ გალახვა არაგცდება

print("საშუალო არითმეტიკული:", average)
print("აღემატება თუ არა 5-ს", exceeds_five)
print("გელის თუ არა სახლში გალახვა?", will_get_punished)


#11
#არასწორი
#num1 = input("Enter first number: ")
#num2 = int(input("Enter second number: "))
#result = num1 + num2
#print(result)

#სწორი
num1 = int(input("Enter first number: "))  # int მივამატე
num2 = int(input("Enter second number: "))

result = num1 + num2
print(result)


#არასწორი 
#num1 = int(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#result = num1 - "5" * num2
#print(result)

#სწორი
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# მოვხსენი ბრჭყალები რომ რიცხვი იყოს
result = num1 - 5 * num2
print(result)


#არასწორი 
#hours = input("Enter hours worked: ")
#rate = float(input("Enter hourly rate: "))
#bonus = input("Enter bonus: ")
#salary = hours * rate
#total = salary + bonus
#final_salary = total / "2"
#print(final_salary)

#სწორი
hours = float(input("Enter hours worked: ")) #float დავამატე
rate = float(input("Enter hourly rate: "))
bonus = float(input("Enter bonus: ")) #აქაც 

salary = hours * rate
total = salary + bonus
final_salary = total / 2  # ბრჭყალები მოვხსენი რომ რიცხვი იყოს

print(final_salary)


#არასწორი
#price = float(input("Enter product price: "))
#quantity = input("Enter quantity: ")
#discount = float(input("Enter discount percentage: "))
#subtotal = price + quantity
#discount_amount = subtotal * discount
#final_price = subtotal - "10"
#print(int(final_price))

#სწორი
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))  # int დავამატე რომ რიცხვი იყოს
discount = float(input("Enter discount percentage: "))

subtotal = price * quantity  # მიმატების ნაცვლად ფასი მრავლდება რაოდენობაზე
discount_amount = subtotal * discount
final_price = subtotal - 10  # ბრჭყალები მოვხსენი

print(int(final_price))


#არასწორი
#num1 = int(input("Enter first number: "))
#num2 = input("Enter second number: ")
#num3 = float(input("Enter third number: "))
#total = num1 + num2
#average = total / num3
#remainder = average % "2"
#result = int(remainder + num1)
#print(result)

#სწორი
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  # int დავამატე რომ რიცხვი იყოს
num3 = float(input("Enter third number: "))

total = num1 + num2
average = total / num3
remainder = average % 2  # ბრჭყალები მოვხსენი 
result = int(remainder + num1)

print(result)








