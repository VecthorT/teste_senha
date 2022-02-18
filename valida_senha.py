from os import system

def valida_caracteres(valor):
    n, maius, minus, esp = False, False, False, False
    for letra in valor:
        if letra.isdigit():
            n = True
            break
    for letra in valor:
        if letra.islower():
            minus = True
            break
    for letra in valor:
        if letra.isupper():
            maius = True
            break
    for letra in valor:
        if letra in caractere_especial():
            esp = True
            break
    if n and maius and minus and esp:
        return(True)
    else:
        inform_erro(n,maius,minus,esp)
        return(False)
def caractere_especial():
    arquivo = open('instrucoes.txt', 'r', encoding='UTF-8')
    caract = arquivo.readlines()
    caract_spc = caract[6].split()
    arquivo.close()
    return(caract_spc[4])
def inform_erro(n,maius,minus,esp):
    system('cls')
    print('Senha Inválida, sua senha deve: ')
    if not n:
        print('Conter no mínimo 1 digito. [X]')
    if not maius:
        print('Conter no mínimo 1 letra em maiúsculo. [X]')
    if not minus:
        print('Conter no mínimo 1 letra em minúsculo. [X]')
    if not esp:
        print('Conter caracteres especiais: !@#$%^&*()-+ [X]')
    