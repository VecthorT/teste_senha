from valida_senha import valida_caracteres
from os import system
def caractere_especial():
    arquivo = open('instrucoes.txt', 'r', encoding='UTF-8')
    caract = arquivo.readlines()
    caract_spc = caract[6].split()
    arquivo.close()
    return(caract_spc[4])
def instru():
    arquivo = open('instrucoes.txt', 'r', encoding='UTF-8')
    for linha in arquivo.readlines():
        print(linha.strip())
    print()
    arquivo.close()
    recebe_senha()
def recebe_senha():
    valida_senha(input(str('Digite sua Senha: ')))
def valida_senha(valor):
    system('cls')
    if len(valor) < 6:
        print('Senha muito curta')
        print(f'Faltam {6 - len(valor)} caracteres')
        recebe_senha()
    elif not valida_caracteres(valor):
        recebe_senha()
    else:
        system('cls')
        print('Senha Válida')