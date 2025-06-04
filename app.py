import os 

# Variavel global
lista_restaurantes = []

def exibe_titulo():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibe_menu():
    print("1- Cadastrar restaurante")
    print("2- Listar restaurantes")
    print("3- Ativar restaurante")
    print("4- Sair\n")

def escolher_opcao():
    # try e uma funcao que permite tratar erros de entrada do usuario
    # except e uma palavra reservada que captura o erro
    try:
        opcao_escolhida = int(input("Escolha uma opcao: "))
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def voltar_ao_menu_principal():
    input("\nPressione enter para voltar ao menu principal...")
    main()

def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de Restaurante")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    lista_restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de Restaurantes")
    for restaurante in lista_restaurantes:
        print(f"- {restaurante}")
    
    voltar_ao_menu_principal()
    
def opcao_invalida():
    print("Opcao invalida!")
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo("Finalizando o aplicativo")

def main():
    os.system("cls")
    exibe_titulo()
    exibe_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()