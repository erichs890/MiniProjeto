from controllers.AlunoController import AlunoController
from alunosFiltro import *


class AlunoView:
    def listar_alunos(self, nomes_historia):
        contador = 0
        for nome in nomes_historia:
            print(nome)
            contador += 1
        print(f"{contador} pessoas")
