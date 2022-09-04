import random
from secrets import choice
import string

escolhaUsuario = 1
senha = list(string.ascii_letters + string.digits + string.ascii_uppercase + "!$@#&")

def gerarSenha():
    random.shuffle(senha)

    senhaa = []

    tamanhoSenha = int(input("Qual o tamanho que você quer da sua senha?\n"))

    for i in range(tamanhoSenha):
        senhaa.append(random.choice(senha))

    random.shuffle(senhaa)

    print("Sua senha é: ")
    print("".join(senhaa) + "\n")

while escolhaUsuario != 0:
    escolhaUsuario = int(input("Deseja gerar uma senha? (1 para SIM e 0 para NÃO)\n"))
    if (escolhaUsuario == 1):
        gerarSenha()