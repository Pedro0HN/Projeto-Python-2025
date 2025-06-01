espacos_lista=[
    ("Salão De Festas"),
    ("Churrascaria"),
    ("Salão Gourmet"),
    ("Piscina")
]

reservas = []

def especial(a):
    contador = len(a)
    print('-' * contador)
    print(a)
    print('-' * contador)

def adicionar_reserva():
    nome = str(input("Digite seu nome: ")).capitalize()
    if not nome.isalpha():
        print('Nome Inválido')
        return
    sobrenome = str(input("Digite seu sobrenome: ")).title()
    if not sobrenome.isalpha():
        print('Sobrenome Inválido')
        return

    nome_sobrenome = nome + ' ' + sobrenome

    print('''
    [0] - Salâo de Festas
    [1] - Churrascaria
    [2] - Salão Gourmet 
    [3] - Piscina 
    ''')
    espaco = int(input("Digite o número respectivo ao espaço que será reservado: "))
    if espaco < 0 or espaco >= len(espacos_lista):
        print('Número invalido')
        return
    else:
        espaco=espacos_lista[espaco]
    ano = int(input("Digite a ano da reserva (2025-2030): "))
    if ano < 2025 or ano>2030:
        print("Ano inválido ou não registrado no sistema")
        return
    mes = int(input("Digite o mês da reserva: "))
    if mes < 1 or mes > 12:
        print('Número do mês inválido')
        return
    if mes == 2:
        dia = int(input("Digite o dia da reserva (1-28): "))
        if dia < 1 or dia > 28:
            print('Dia inválido')
            return
    else:
        dia = int(input("Digite o dia da reserva (1-30): "))
        if dia < 1 or dia > 30:
         print('Dia inválido')
         return

    data = f"{dia:02d}/{mes:02d}/{ano}"

    for r in reservas:
        if r[1] == espaco and r[2] == data:
            especial(f"O espaço {espaco} já está reservado na data {data}.")
            return
    reservas.append((nome_sobrenome , espaco, data))
    especial(f"Reserva confirmada para {nome_sobrenome} no(a) {espaco} em {data}.")

def listar_reservas():
    if reservas:
        especial("Reservas Confirmadas:")
        for (nome, espaco, data) in reservas:
            especial(f"{nome} reservou o {espaco} para {data}")
    else:
        especial("Nenhuma reserva realizada.")

def cancelar_reserva():
    nome = str(input("Digite o nome da reserva a ser cancelada: ")).capitalize()
    if not nome.isalpha():
        print('Nome Inválido')
        return
    sobrenome = str(input("Dgitte o sobrenome da reserva a ser cancelada: ")).title()
    if not sobrenome.isalpha():
        print('Sobrenome Inválido')
        return
    nome_sobrenome = nome + ' ' + sobrenome
    print('''
        [0] - Salâo de Festas
        [1] - Churrascaria
        [2] - Salão Gourmet 
        [3] - Piscina
        ''')
    espaco = int(input("Digite o número do espaço a ser cancelado: "))
    if espaco < 0 or espaco >= len(espacos_lista):
        print('Número invalido')
        return
    else:
        espaco=espacos_lista[espaco]
    ano = int(input("Digite o ano da reserva a ser cancelado (2025-2030): "))
    if ano < 2025 or ano>2030:
        print("Ano inválido ou não registrado no sistema")
        return
    mes = int(input(" Digite o mes da reserva a ser cancelado: "))
    if mes < 1 or mes > 12:
        print('Número do mês inválido')
        return
    dia = int(input("Digite o dia da reserva a ser cancelado (1-30): "))
    if mes==2:
        if dia < 1 or dia>28:
            print('Dia inválido')
            return
    elif dia < 1 or dia > 30:
        print('Dia inválido')
        return

    data = f"{dia:02d}/{mes:02d}/{ano}"

    comparacao = (nome_sobrenome, espaco, data)
    if comparacao in reservas:
        reservas.remove(comparacao)
        especial(f"Reserva de {nome_sobrenome} no {espaco} para a data {data} cancelada com sucesso.")
    else:
        especial(f"Não há reserva de {nome_sobrenome} no {espaco} na data {data}.")

def menu():
    while True:
        print("\nMenu de Reservas")
        print("1. Adicionar Reserva")
        print("2. Listar Reservas")
        print("3. Cancelar Reserva")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_reserva()
        elif opcao == '2':
            listar_reservas()
        elif opcao == '3':
            cancelar_reserva()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
