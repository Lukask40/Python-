import os
import time
from dataclasses import dataclass
os.system("cls || clear")  # Limpa o terminal em windows e Linux.

lista_clientes = []
lista_produtos = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}")

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: str
    validade: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nQuantidade: {self.quantidade} \nLote: {self.lote} \nValidade: {self.validade}")

# Função para verificar se a lista de clientes está vazia
def lista_esta_vazia(lista):
    if not lista:
        print("\nNão há dados cadastrados.")
        return True
    return False

# Função para adicionar um novo cliente
def adicionar_cliente():
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

# Função para adicionar um novo produto
def adicionar_produto():
    print("\n--- Adicionar novo produto ---")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    lote = input("Digite o número do lote: ")
    validade = input("Digite a validade do produto (ex: 2025-12-31): ")

    novo_produto = Produto(nome=nome, quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)
    print(f"\nProduto {nome} adicionado com sucesso!")

# Função para mostrar todos os clientes
def mostrar_todos_clientes():
    if lista_esta_vazia(lista_clientes):
        return
    print("\n--- Lista de clientes ---")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

# Função para mostrar todos os produtos
def mostrar_todos_produtos():
    if lista_esta_vazia(lista_produtos):
        return
    print("\n--- Lista de produtos ---")
    for produto in lista_produtos:
        produto.mostrar_dados()

# Função para atualizar dados de um cliente
def atualizar_cliente():
    if lista_esta_vazia(lista_clientes):
        return

    print("--- Atualizar dados de clientes ---")
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(nome_buscar)

    if cliente_para_atualizar:
        print("\nCliente encontrado.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nEmail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo email: ")

        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print("\nDados atualizados com sucesso!")
    else:
        print("\nCliente não encontrado.")

# Função para atualizar dados de um produto
def atualizar_produto():
    if lista_esta_vazia(lista_produtos):
        return

    print("--- Atualizar dados de produto ---")
    nome_buscar = input("\nDigite o nome do produto: ")
    produto_para_atualizar = encontrar_produto_por_nome(nome_buscar)

    if produto_para_atualizar:
        print("\nProduto encontrado.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {produto_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nQuantidade atual: {produto_para_atualizar.quantidade}")
        nova_quantidade = input("Nova quantidade: ")

        print(f"\nLote atual: {produto_para_atualizar.lote}")
        novo_lote = input("Novo lote: ")

        print(f"\nValidade atual: {produto_para_atualizar.validade}")
        nova_validade = input("Nova validade: ")

        if novo_nome:
            produto_para_atualizar.nome = novo_nome
        if nova_quantidade:
            produto_para_atualizar.quantidade = int(nova_quantidade)
        if novo_lote:
            produto_para_atualizar.lote = novo_lote
        if nova_validade:
            produto_para_atualizar.validade = nova_validade

        print("\nDados atualizados com sucesso!")
    else:
        print("\nProduto não encontrado.")

# Função para excluir um cliente
def excluir_cliente():
    if lista_esta_vazia(lista_clientes):
        return

    mostrar_todos_clientes()

    nome_buscar = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_nome(nome_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\nCliente {nome_buscar} não encontrado!")

# Função para excluir um produto
def excluir_produto():
    if lista_esta_vazia(lista_produtos):
        return

    mostrar_todos_produtos()

    nome_buscar = input("\nDigite o nome do produto que deseja excluir: ")

    produto_para_remover = encontrar_produto_por_nome(nome_buscar)

    if produto_para_remover:
        lista_produtos.remove(produto_para_remover)
        print(f"\nProduto {produto_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\nProduto {nome_buscar} não encontrado!")

# Função para encontrar um cliente pelo nome
def encontrar_cliente_por_nome(nome_buscar):
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar.lower():
            return cliente
    return None

# Função para encontrar um produto pelo nome
def encontrar_produto_por_nome(nome_buscar):
    for produto in lista_produtos:
        if produto.nome.lower() == nome_buscar.lower():
            return produto
    return None

# Menu principal
while True:
    print("""
          --- Gerenciador de Clientes e Produtos ---
          1 - Gerenciar Clientes
          2 - Gerenciar Produtos
          0 - Sair
          """)

    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    if opcao == 1:
        while True:
            print("""
                --- Gerenciador de Clientes ---
                1 - Adicionar Cliente
                2 - Mostrar Todos Clientes
                3 - Atualizar Cliente
                4 - Excluir Cliente
                0 - Voltar
            """)
            try:
                opcao_cliente = int(input("Escolha uma opção: "))
            except ValueError:
                print("\nEntrada inválida. Digite um número...")
                time.sleep(2)
                os.system("cls || clear")
                continue

            if opcao_cliente == 1:
                adicionar_cliente()
            elif opcao_cliente == 2:
                mostrar_todos_clientes()
            elif opcao_cliente == 3:
                atualizar_cliente()
            elif opcao_cliente == 4:
                excluir_cliente()
            elif opcao_cliente == 0:
                break
            else:
                print("\nOpção inválida. Tente novamente.")
            time.sleep(2)
            os.system("cls || clear")

    elif opcao == 2:
        while True:
            print("""
                --- Gerenciador de Produtos ---
                1 - Adicionar Produto
                2 - Mostrar Todos Produtos
                3 - Atualizar Produto
                4 - Excluir Produto
                0 - Voltar
            """)
            try:
                opcao_produto = int(input("Escolha uma opção: "))
            except ValueError:
                print("\nEntrada inválida. Digite um número...")
                time.sleep(2)
                os.system("cls || clear")
                continue

            if opcao_produto == 1:
                adicionar_produto()
            elif opcao_produto == 2:
                mostrar_todos_produtos()
            elif opcao_produto == 3:
                atualizar_produto()
            elif opcao_produto == 4:
                excluir_produto()
            elif opcao_produto == 0:
                break
            else:
                print("\nOpção inválida. Tente novamente.")
            time.sleep(2)
            os.system("cls || clear")

    elif opcao == 0:
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
    time.sleep(2)
    os.system("cls || clear")

    