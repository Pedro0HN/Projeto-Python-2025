import os
from datetime import datetime


def especial(a):
    contador = len(a)
    print('-' * contador)
    print(a)
    print('-' * contador)


def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return [eval(linha.strip()) for linha in arquivo.readlines() if linha.strip()]
    return []


def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for item in dados:
            arquivo.write(str(item) + '\n')


def adicionar_reserva(reservas, espacos_lista):
    nome = str(input("      Digite seu nome: ")).capitalize()
    sobrenome = str(input("      Digite seu sobrenome: "))


    nome_sobrenome = nome + ' ' + sobrenome

    print('''
      [0] - Salâo de Festas
      [1] - Churrascaria
      [2] - Salão Gourmet 
      [3] - Piscina 
    ''')
    try:
        espaco = int(input("      Digite o número respectivo ao espaço que será reservado: "))
        if espaco < 0 or espaco >= len(espacos_lista):
            print('Número inválido')
            return reservas
        espaco = espacos_lista[espaco]
    except ValueError:
        print('Número inválido')
        return reservas

    try:
        ano = int(input("      Digite o ano da reserva (2025-2030): "))
        if ano < 2025 or ano > 2030:
            print("      Ano inválido ou não registrado no sistema")
            return reservas
        mes = int(input("      Digite o mês da reserva: "))
        if mes < 1 or mes > 12:
            print('      Número do mês inválido')
            return reservas
        if mes == 2:
            dia = int(input("      Digite o dia da reserva (1-28): "))
            if dia < 1 or dia > 28:
                print('      Dia inválido')
                return reservas
        else:
            dia = int(input("      Digite o dia da reserva (1-30): "))
            if dia < 1 or dia > 30:
                print('      Dia inválido')
                return reservas
        datetime.strptime(f"{dia:02d}/{mes:02d}/{ano}", '%d/%m/%Y')
    except ValueError:
        print("      Data inválida")
        return reservas

    data = f"{dia:02d}/{mes:02d}/{ano}"

    for r in reservas:
        if r[1] == espaco and r[2] == data:
            especial(f"O espaço {espaco} já está reservado na data {data}.")
            return reservas
    reservas.append((nome_sobrenome, espaco, data))
    print(r"""
  _________  _  _____________  __  ______   ___  ____ 
 / ___/ __ \/ |/ / __/  _/ _ \/  |/  / _ | / _ \/ __ \
/ /__/ /_/ /    / _/_/ // , _/ /|_/ / __ |/ // / /_/ /
\___/\____/_/|_/_/ /___/_/|_/_/  /_/_/ |_/____/\____/ 

""")
    especial(f"Reserva confirmada para {nome_sobrenome} no(a) {espaco} em {data}.")
    return reservas


def listar_reservas(reservas):
    if reservas:
        print(r"""
       __         ____                                      __      __
      / /___ _   / __ \___  ________  ______   ______ _____/ /___  / /
 __  / / __ `/  / /_/ / _ \/ ___/ _ \/ ___/ | / / __ `/ __  / __ \/ / 
/ /_/ / /_/ /  / _, _/  __(__  )  __/ /   | |/ / /_/ / /_/ / /_/ /_/  
\____/\__,_/  /_/ |_|\___/____/\___/_/    |___/\__,_/\__,_/\____(_)   

""")
        for (nome, espaco, data) in reservas:
            especial(f"{nome} reservou {espaco} para {data}")
    else:
        especial("Nenhuma reserva realizada.")
    return reservas


def cancelar_reserva(reservas, espacos_lista):
    nome = str(input("Digite o nome da reserva a ser cancelada: ")).capitalize()
    if not nome.isalpha():
        print('Nome Inválido')
        return reservas
    sobrenome = str(input("Digite o sobrenome da reserva a ser cancelada: ")).title()
    if not sobrenome.isalpha():
        print('Sobrenome Inválido')
        return reservas
    nome_sobrenome = nome + ' ' + sobrenome
    print('''
        [0] - Salâo de Festas
        [1] - Churrascaria
        [2] - Salão Gourmet 
        [3] - Piscina
        ''')
    try:
        espaco = int(input("Digite o número do espaço a ser cancelado: "))
        if espaco < 0 or espaco >= len(espacos_lista):
            print('Número inválido')
            return reservas
        espaco = espacos_lista[espaco]
    except ValueError:
        print('Número inválido')
        return reservas
    try:
        ano = int(input("Digite o ano da reserva a ser cancelado (2025-2030): "))
        if ano < 2025 or ano > 2030:
            print("Ano inválido ou não registrado no sistema")
            return reservas
        mes = int(input("Digite o mês da reserva a ser cancelado: "))
        if mes < 1 or mes > 12:
            print('Número do mês inválido')
            return reservas
        dia = int(input("Digite o dia da reserva a ser cancelado (1-30): "))
        if mes == 2:
            if dia < 1 or dia > 28:
                print('Dia inválido')
                return reservas
        elif dia < 1 or dia > 30:
            print('Dia inválido')
            return reservas
        datetime.strptime(f"{dia:02d}/{mes:02d}/{ano}", '%d/%m/%Y')
    except ValueError:
        print("Data inválida")
        return reservas

    data = f"{dia:02d}/{mes:02d}/{ano}"

    comparacao = (nome_sobrenome, espaco, data)
    if comparacao in reservas:
        reservas.remove(comparacao)
        print(r"""
                   _____                                 __
                  / ___/__  __________  ______________  / /
                  \__ \/ / / / ___/ _ \/ ___/ ___/ __ \/ / 
                 ___/ / /_/ / /__/  __(__  |__  ) /_/ /_/  
                /____/\__,_/\___/\___/____/____/\____(_)   

                """)
        especial(f"Reserva de {nome_sobrenome} no {espaco} para a data {data} cancelada com sucesso.")
    else:
        especial(f"Não há reserva de {nome_sobrenome} no {espaco} na data {data}.")
    return reservas