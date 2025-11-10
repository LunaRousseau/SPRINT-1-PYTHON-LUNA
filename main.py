from funcoes import cadastrar_informacao, listar_informacoes, pesquisar_por_tipo

def exibir_menu():
    print("\n=== TOTEM FLEXMEDIA ===")
    print("1 - Cadastrar informação")
    print("2 - Listar informações cadastradas")
    print("3 - Pesquisar informações por tipo")
    print("0 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_informacao()
        elif opcao == "2":
            listar_informacoes()
        elif opcao == "3":
            pesquisar_por_tipo()
        elif opcao == "0":
            print("\nEncerrando o programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()