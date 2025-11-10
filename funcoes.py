informacoes = []

def validar_tipo(tipo):
    tipos_validos = ["educativo", "cultural", "lazer"]
    return tipo.lower() in tipos_validos

def cadastrar_informacao():
    print("\n=== Cadastro de Nova Informação ===")
    titulo = input("Digite o título da informação: ").strip()
    while titulo == "":
        print("O título não pode ficar vazio!")
        titulo = input("Digite o título da informação: ").strip()
    tipo = input("Digite o tipo (educativo / cultural / lazer): ").strip().lower()
    while not validar_tipo(tipo):
        print("Tipo inválido! Escolha entre educativo, cultural ou lazer.")
        tipo = input("Digite o tipo (educativo / cultural / lazer): ").strip().lower()
    descricao = input("Digite uma breve descrição: ").strip()
    informacoes.append({'titulo': titulo, 'tipo': tipo, 'descricao': descricao})
    print("Informação cadastrada com sucesso!\n")

def listar_informacoes():
    print("\n=== Lista de Informações Cadastradas ===")
    if not informacoes:
        print("Nenhuma informação cadastrada ainda.")
        return
    for i, info in enumerate(informacoes, start=1):
        print(f"\n[{i}] {info['titulo'].upper()}")
        print(f"Tipo: {info['tipo'].capitalize()}")
        print(f"Descrição: {info['descricao']}")

def pesquisar_por_tipo():
    print("\n=== Pesquisa de Informações por Tipo ===")
    tipo = input("Digite o tipo desejado (educativo / cultural / lazer): ").strip().lower()
    while not validar_tipo(tipo):
        print("Tipo inválido! Escolha entre educativo, cultural ou lazer.")
        tipo = input("Digite o tipo desejado (educativo / cultural / lazer): ").strip().lower()
    encontrados = [info for info in informacoes if info["tipo"] == tipo]
    if encontrados:
        print(f"\n=== Resultados para tipo '{tipo}' ===")
        for i, info in enumerate(encontrados, start=1):
            print(f"\n[{i}] {info['titulo'].upper()}")
            print(f"Descrição: {info['descricao']}")
    else:
        print(f"Nenhuma informação encontrada para o tipo '{tipo}'.")