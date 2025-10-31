import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Autor:
    nome : str
    biografia : str

@dataclass
class Livro:
    titulo: str
    ano : int
    autor : Autor

    def exibir_detalhes(self):
        print("\n====Detalhes====")
        print(f"Titulo do livro: {self.titulo}")
        print(f"Ano do livro: {self.ano}")
        print(f"Nome do autor: {self.autor.nome}")
        print(f"Biografia do autor: {self.autor.biografia}")


autor1=Livro(titulo=input("Digite o titulo do livro:"),
            ano=int(input("Digite o ano do livro:")),
            autor=Autor(nome=input("Digite o nome do autor:"), biografia=input("Digite a biografia do autor:")))


autor1.exibir_detalhes()



               