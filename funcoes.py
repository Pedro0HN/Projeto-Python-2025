def especial(a):          # Coloca os " _ " para dar um estilo.
    contador = len(a)
    print('-' * contador)
    print(a)
    print('-' * contador)

def adicionar_reserva():
    nome = str(input("Digite seu nome: ")).capitalize() # .capitalize() = Deixa a primeira letra maiúscula.
    if not nome.isalpha():  # .isalpha() = Permite apenas letras (msm o número sendo uma string).
        print('Nome Inválido')
        return
    sobrenome = str(input("Digite seu sobrenome: ")).title() # .title() = Deixa a primeira letras das palavras maiúsculas.
    if not sobrenome.isalpha():
        print('Sobrenome Inválido')
        return

    nome_sobrenome = nome + ' ' + sobrenome   # junta o nome com o sobrenome

    print('''
    [0] - Salâo de Festas
    [1] - Churrasqueira
    [2] - Salão Gourmet 
    [3] - Sala de Jogos
    ''')
    espaco = int(input("Digite o número respectivo ao espaço que será reservado: "))
    if espaco < 0 or espaco >= len(espacos_lista):
        print('Número invalido')
        return
    else:
        espaco=espacos_lista[espaco]    # Adiociona o espaço da lista 'espaco_lista' a 'espaco' conforme a escolha

    ano = int(input("Digite a ano da reserva (2025-2030): "))
    if ano < 2025 or ano>2030:    # Até 2030 pois não acho que da pra fazer uma reserva pra dps de 5 anos
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

    data = f"{dia:02d}/{mes:02d}/{ano}"   # formata dia, mes e ano numa só variável

    arquivo = open('exe.txt', 'r', encoding='utf-8')
    print(arquivo.read())
    sn = str(input("Concorda com os termos acima?('S'/'N'): ")).upper()
    if not sn.isalpha():
        print('Resposta Inválida')
        return
    elif sn=='N':
        print("Termos negados, reserva cancelada.")
        return
    elif sn=='S':
        print("Termos aceitos com sucesso!")
    else:
        print("Resposta Inválida")
        return

    for r in reservas:
        if r[1] == espaco and r[2] == data:   # \se uma reserva estiver no msm espaço e data, a que está sendo feita é cancelada
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
        [1] - Churrasqueira
        [2] - Salão Gourmet 
        [3] - Sala de Jogos
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
