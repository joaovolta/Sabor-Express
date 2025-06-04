import os 

# Variavel global
# lista_restaurantes = []

# Dicionario para armazenar os restaurantes
lista_restaurantes = [
    {"nome": "Coco Bambu", "categoria": "Francesa", "Ativo": False}, 
    {"nome": "Outback", "categoria": "Americana", "Ativo": False},
    {"nome": "Madero", "categoria": "Brasileira", "Ativo": False}
]

def exibe_titulo():
    """Exibe o titulo do aplicativo na tela"""

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibe_menu():
    """Exibe o menu principal do aplicativo"""

    print("1- Cadastrar restaurante")
    print("2- Listar restaurantes")
    print("3- Alternar estado do restaurante")
    print("4- Sair\n")

def escolher_opcao():
    """Escolhe uma das opcoes do menu principal e executa a funcao correspondente"""

    # try e uma funcao que permite tratar erros de entrada do usuario
    # except e uma palavra reservada que captura o erro
    try:
        opcao_escolhida = int(input("Escolha uma opcao: "))
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    """Exibe um subtitulo na tela com o texto passado como paramentro"""

    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    """Exibe uma mensagem de volta ao menu principal e apos isso volta ao menu principal"""
    
    input("\nPressione enter para voltar ao menu principal...")
    main()

def cadastrar_restaurante():
    """
    Cadastra um novo restaurante na lista de restaurantes

    inputs: 
        - Nome do restaurante
        - Categoria do restaurante

    outputs:
        - Armazena os dados do restautante em um dicionario e depois adiciona esse dicionario na lista de restaurantes
        - Exibe uma mensagem de sucesso ao cadastrar o restaurante
    """

    exibir_subtitulo("Cadastro de Restaurante")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    # dados_restaurante armazena os dados do restaurante em um dicionario
    dados_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "Ativo": False}
    # Adiciona o dicionario dados_restaurante na lista lista_restaurantes
    lista_restaurantes.append(dados_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Lista todos os restaurantes cadastrados na lista de restaurantes"""

    exibir_subtitulo("Lista de Restaurantes")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Estado"}")
    for restaurante in lista_restaurantes:
        nome_do_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        # Verifica se o restaurante esta ativo ou desativado
        # Se o restaurante estiver ativo, exibe "Ativo", caso contrario exibe "Desativado"
        ativo = "Ativo" if restaurante["Ativo"] else "Desativado"

        print(f"- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """Ativa ou desativa um restaurante cadastrado na lista de restaurantes"""

    exibir_subtitulo("Ativar/Desativar Restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_do_restaurante == restaurante["nome"]:
            restaurante_encontrado = True 
            restaurante["Ativo"] = not restaurante["Ativo"] # Inverte o estado do restaurante
            mensagem = f"O restaurante {nome_do_restaurante} foi ativado com sucesso!" if restaurante["Ativo"] == True else f"O restaurante {nome_do_restaurante}foi desativado com sucesso!"  
            print(mensagem)
    
    # Se o restaurante nao for encontrado, exibe uma mensagem de erro
    if not restaurante_encontrado:
        print(f"O restaurante {nome_do_restaurante} nao foi encontrado!")
    
    voltar_ao_menu_principal()

def opcao_invalida():
    """Exibe uma mensagem de erro quando a opcao escolhida nao for valida"""

    print("Opcao invalida!")
    voltar_ao_menu_principal()

def finalizar_app():
    """Exibe uma mensagem de finalizacao do aplicativo e encerra o programa"""
    
    exibir_subtitulo("Finalizando o aplicativo")

def main():
    os.system("cls")
    exibe_titulo()
    exibe_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()