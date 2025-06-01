from funções import especial
from funções import adicionar_reserva
from funções import listar_reservas
from funções import cancelar_reserva
espacos_lista=[
    ("Salão De Festas"),
    ("Churrascaria"),
    ("Salão Gourmet"),
    ("Piscina")
]
reservas = []

def menu():
    while True:
        print("\nMenu de Reservas")
        print("1. Adicionar Reserva")
        print("2. Listar Reservas")
        print("3. Cancelar Reserva")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_reserva(reservas, espacos_lista)
        elif opcao == '2':
            listar_reservas(reservas)
        elif opcao == '3':
            cancelar_reserva(reservas, espacos_lista)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
