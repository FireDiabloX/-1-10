import random
print("Вгадай число від 1 до 10")
number= random.randint(1, 10)
attempts = 3
while attempts > 0:
    print(f"\nЗалишилось спроб: {attempts}")
    guess = int(input("Введіть ваше число: "))
    if guess == number:
        print("Вітаю ви вгадали число!")
        break
    elif guess < number:
        print("Ваше число менше загаданого")
    else:
        print("Ваше число більше загаданого")

    attempts -= 1
    if attempts == 0:
        print(f"Ви програли! У вас кінчились спроби.Загадане число було:{number}")