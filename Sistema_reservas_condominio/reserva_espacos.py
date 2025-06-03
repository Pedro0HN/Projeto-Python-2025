from funcoes import adicionar_reserva, listar_reservas, cancelar_reserva

espacos_lista = [
    "Salão De Festas",
    "Churrascaria",
    "Salão Gourmet",
    "Piscina"
]

reservas = []


def menu():
    while True:
        print(r"""
            ____                                      
           / __ \___  ________  ______   ______ ______
          / /_/ / _ \/ ___/ _ \/ ___/ | / / __ `/ ___/
         / _, _/  __(__  )  __/ /   | |/ / /_/ (__  ) 
        /_/ |_|\___/____/\___/_/    |___/\__,_/____/  

        ,_     _
        |\\_,-~/             1.   Adicionar Reserva
        / _  _ |    ,--.     2.   Listar Reservas
       (  @  @ )   / ,-'     3.   Cancelar Reserva
        \  _T_/-._( (        4.   Sair
        /         `. \
       |         _  \ |
        \ \ ,  /      |
         || |-_\__   /
       ((_/`(____,-'
        """)

        opcao = input("      Escolha uma opção: ")

        if opcao == '1':
            adicionar_reserva(reservas, espacos_lista)

        elif opcao == '2':
            listar_reservas(reservas)

        elif opcao == '3':
            cancelar_reserva(reservas)

        elif opcao == '4':
            print(r"""
  ______     __                               
 /_  __/____/ /_  ____ ___  __                
  / / / ___/ __ \/ __ `/ / / /                
 / / / /__/ / / / /_/ / /_/ / _ _ _ _ _ _ _ _ 
/_/  \___/_/ /_/\__,_/\__,_(_|_|_|_|_|_|_|_|_)

                 ,,__
        ..  ..   / o._)                   .---.
       /--'/--\  \-'||        .----.    .'     '.
      /        \_/ / |      .'      '..'         '-.
    .'\  \__\  __.'.'     .'          ě-._
      )\ |  )\ |      _.'  
     // \\ // \\          
    ||_  \\|_  \\_        
    '--' '--'' '--'                                         

""")
            break

        else:
            print("Opção inválida. Tente novamente.\n")


menu()
