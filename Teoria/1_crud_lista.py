import os
os.system("cls|| clear")
#CRUD usando lista.
#Create = criar / salvar
#Read = buscar / selecionar
# Update atualizar / modifica
# Delete = excluir
#Criando uma lista.
lista_clientes = []

print("CREATE - Adicionar / Inserir ")
nome = "Marta"
lista_clientes.append(nome)
print(f"O nome: {nome} foi inserido com sucesso!")

#Read
print("\nRead - Ler / Moatar")
print(lista_clientes)

#Update
print("\nUpdate - Atualizar / Alterar")
nome_para_atulizar = "Marta" 
if nome_para_atulizar in lista_clientes:
    novo_nome = "Marta Silva"
    indice = lista_clientes.index(nome_para_atulizar)
    lista_clientes [indice] = novo_nome
    print(f"O nome {nome_para_atulizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atulizar} não foi encontrado.")
          
print(lista_clientes)
#DELETE
print("\nDelete Excluir / Remover")
nome_para_excluir = "Maria"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluido com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontratio.")

print(lista_clientes)