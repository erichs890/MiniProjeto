from serviços.AlunoServico import AlunoServico
from alunosFiltro import AlunosFiltro
from views.AlunoView import AlunoView

class AlunoController:
    def __init__(self, url):
        self.aluno_servico = AlunoServico(url)
        self.filtro = AlunosFiltro()
        self.view = AlunoView()

    def listar_alunos_historia(self):
        # Obtém os alunos do serviço
        dados = self.aluno_servico.getAlunos()
        
        # Aplica o filtro para alunos de História na modalidade Presencial
        alunos_historia = self.filtro.filtroHistoria(dados)
        
        # Passa os alunos filtrados para a view
        self.view.listar_alunos(alunos_historia)
