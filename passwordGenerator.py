import random
from secrets import choice
import string

userChoice = 1
password = list(string.ascii_letters + string.digits + string.ascii_uppercase + "!$@#&")

def gerarSenha():
    random.shuffle(password)

    passwordd = []

    lengthPassword = int(input("How long do you want your password?\n"))

    for i in range(lengthPassword):
        passwordd.append(random.choice(password))

    random.shuffle(passwordd)

    print("You password is: ")
    print("".join(passwordd) + "\n")

while userChoice != 0:
    userChoice = int(input("Do you want to generate password? (1 for YES and 0 for NO)\n"))
    if (userChoice == 1):
        gerarSenha()