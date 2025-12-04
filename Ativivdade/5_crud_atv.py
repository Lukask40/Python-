import os
import time
from dataclasses import dataclass

os.system("cls || clear")  # Limpa o terminal em Windows e Linux.

lista_alunos = []

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str

@dataclass
class Aluno:
    nome: str
    curso: str
    matricula: str  # RA do aluno
    data_nascimento: str  # Data de nascimento no formato dd/mm/aaaa
    endereco: Endereco

    def mostrar_dados(self):
        return (f"Nome: {self.nome}\nCurso: {self.curso}\nMatrícula (RA): {self.matricula}\n"
                f"Data de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco.logradouro}, "
                f"{self.endereco.numero}, {self.endereco.cidade} - {self.endereco.estado}")

# Função para verificar se a lista de alunos está vazia
def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNão há alunos cadastrados.")
        return True
    return False

# Função para adicionar um novo aluno na lista
def adicionar_aluno(lista_alunos):
    print("\n--- Adicionar novo aluno ---")
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    matricula = input("Digite a matrícula (RA): ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

    # Dados do endereço
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    # Criando instância de Endereço
    endereco = Endereco(logradouro=logradouro, numero=numero, cidade=cidade, estado=estado)

    novo_aluno = Aluno(nome=nome, curso=curso, matricula=matricula, data_nascimento=data_nascimento, endereco=endereco)
    lista_alunos.append(novo_aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")

# Função para encontrar um aluno na lista
def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno
    return None  # Retorna None se o aluno não for encontrado.

# Função para mostrar todos os alunos
def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    print("\n--- Lista de alunos ---")
    for aluno in lista_alunos:
        print(aluno.mostrar_dados())

# Função para atualizar dados de um aluno
def atualizar_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    print("\n--- Atualizar dados de alunos ---")
    nome_buscar = input("\nDigite o nome do aluno: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_atualizar:
        print("\nAluno encontrado.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        novo_nome = input(f"\nNome atual: {aluno_para_atualizar.nome}\nNovo nome: ")
        novo_curso = input(f"\nCurso atual: {aluno_para_atualizar.curso}\nNovo curso: ")
        novo_matricula = input(f"\nMatrícula (RA) atual: {aluno_para_atualizar.matricula}\nNova matrícula (RA): ")
        nova_data_nascimento = input(f"\nData de Nascimento atual: {aluno_para_atualizar.data_nascimento}\nNova data de nascimento (dd/mm/aaaa): ")

        # Atualizando os dados do endereço
        novo_logradouro = input(f"Logradouro atual: {aluno_para_atualizar.endereco.logradouro}\nNovo logradouro: ")
        novo_numero = input(f"Número atual: {aluno_para_atualizar.endereco.numero}\nNovo número: ")
        nova_cidade = input(f"Cidade atual: {aluno_para_atualizar.endereco.cidade}\nNova cidade: ")
        novo_estado = input(f"Estado atual: {aluno_para_atualizar.endereco.estado}\nNovo estado: ")

        # Atualizando os dados do aluno
        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
        if novo_curso:
            aluno_para_atualizar.curso = novo_curso
        if novo_matricula:
            aluno_para_atualizar.matricula = novo_matricula
        if nova_data_nascimento:
            aluno_para_atualizar.data_nascimento = nova_data_nascimento

        # Atualizando os dados de endereço
        if novo_logradouro:
            aluno_para_atualizar.endereco.logradouro = novo_logradouro
        if novo_numero:
            aluno_para_atualizar.endereco.numero = novo_numero
        if nova_cidade:
            aluno_para_atualizar.endereco.cidade = nova_cidade
        if novo_estado:
            aluno_para_atualizar.endereco.estado = novo_estado

        print(f"\nDados do aluno {aluno_para_atualizar.nome} atualizados com sucesso!")
    else:
        print("\nAluno não encontrado.")

# Função para excluir um aluno
def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_alunos(lista_alunos)

    nome_buscar = input("\nDigite o nome do aluno que deseja excluir: ")
    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_remover:
        lista_alunos.remove(aluno_para_remover)
        print(f"\nAluno {aluno_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\nAluno {nome_buscar} não encontrado.")

# Mostrar menu
while True:
    print("""
          --- Gerenciador de Alunos ---
          1 - Adicionar
          2 - Mostrar todos
          3 - Atualizar
          4 - Excluir
          0 - Sair
          """)

    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if opcao != 1 and opcao != 0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls || clear")
