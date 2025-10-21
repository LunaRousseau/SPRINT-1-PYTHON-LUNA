def cadastrar_informacao(lista):
    titulo = input("Digite o título da informação: ")
    tipo = input("Digite o tipo da informação (educativo, cultural, lazer, etc.): ")
    descricao = input("Digite a descrição da informação: ")
    informacao = {
        "titulo": titulo,
        "tipo": tipo,
        "descricao": descricao
    }
    lista.append(informacao)
    print("Informação cadastrada com sucesso!")

def listar_informacoes(lista):
    if not lista:
        print("Nenhuma informação cadastrada ainda.")
        return
    print("\n--- Informações Cadastradas ---")
    for i, info in enumerate(lista):
        print(f"\nInformação #{i+1}")
        print(f"Título: {info['titulo']}")
        print(f"Tipo: {info['tipo']}")
        print(f"Descrição: {info['descricao']}")
    print("------------------------------")

def main():
    informacoes_totem = []
    while True:
        print("\n--- Menu Totem FlexMedia ---")
        print("1 - Cadastrar informação")
        print("2 - Listar informações cadastradas")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_informacao(informacoes_totem)
        elif opcao == '2':
            listar_informacoes(informacoes_totem)
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()