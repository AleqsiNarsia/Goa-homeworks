# შექმენით ბანკომატის PIN კოდის შემოწმების სისტემა: მომხმარებელს შემოაყვანინეთ ბარათის ნომერი (card_number) და PIN კოდი (pin). თუ card_number უდრის "1234-5678"-ს და pin უდრის "4321"-ს, დაბეჭდეთ "Access granted!", სხვა შემთხვევაში კი — "Invalid card or PIN!"

card_number = (input("შეიყვანეთ თქვენი ბარათის PIN: "))
pin = (input("შეიყვანეთ თქვენი PIN: "))

if card_number == "1234-5678" and pin == "4321":
    print("Access granted!")
else:
    print("Invalid card or PIN! ")











