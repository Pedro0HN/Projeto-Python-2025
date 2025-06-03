with open("funcoes.py", "r", encoding="utf-8") as f:
    codigo = f.read()
exec(codigo)

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
