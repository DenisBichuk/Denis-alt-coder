import random

chars = "+-/*!&$#?=@<>abcdefghigklmnopqrstuvqwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890"

number = int(input("Кол-во паролей: "))
length = int(input("Длина строки: "))

for x in range(number):
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print(password)

    file = open("password.txt", "a")
    file.write(password + "\n")
    file.close()
