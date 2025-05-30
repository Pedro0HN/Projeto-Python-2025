
reservas = []

def especial(a):
    contador = len(a)
    print('-' * contador)
    print(a)
    print('-' * contador)

def adicionar_reserva():
    nome = input("Digite seu nome: ")
    espaco = input("Digite o espaço a ser reservado (salão de festas, churrasqueira, salão gourmet): ")
    data = input("Digite a data da reserva (dd/mm/aaaa): ")
    for r in reservas:
        if r[1] == espaco and r[2] == data:
            especial(f"O espaço {espaco} já está reservado na data {data}.")
            return
    reservas.append((nome, espaco, data))
    especial(f"Reserva confirmada para {nome} no {espaco} em {data}.")

def listar_reservas():
    if reservas:
        especial("Reservas Confirmadas:")
        for (nome, espaco, data) in reservas:
            especial(f"{nome} reservou o {espaco} para {data}")
    else:
        especial("Nenhuma reserva realizada.")

def cancelar_reserva():
    nome = input("Digite o nome da pessoa que reservou: ")
    espaco = input("Digite o espaço a ser cancelado (salão de festas, churrasqueira, salão gourmet): ")
    data = input("Digite a data da reserva a ser cancelada (dd/mm/aaaa): ")
    comparacao = (nome, espaco, data)
    if comparacao in reservas:
        reservas.remove(comparacao)
        especial(f"Reserva de {nome} no {espaco} para a data {data} cancelada com sucesso.")
    else:
        especial(f"Não há reserva para {nome} no {espaco} na data {data}.")

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
