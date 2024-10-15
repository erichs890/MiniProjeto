from serviços.AlunoServico import AlunoServico
from modelos.Aluno import Aluno

class AlunoController:
    def __init__(self, servico_aluno):
        self.servico_aluno = servico_aluno

    def get_alunos(self, curso, modalidade):
        dados_alunos = self.servico_aluno.get_alunos(curso, modalidade)
        alunos = [Aluno(**dados) for dados in dados_alunos]
        return alunos

    def get_aluno(self, id):
        dados_aluno = self.servico_aluno.get_aluno(id)
        return Aluno(**dados_aluno)