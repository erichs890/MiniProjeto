from controllers.AlunoController import AlunoController

class AlunoView:
    def __init__(self, controladorAluno):
        self.controladorAluno = controladorAluno

    def listar_alunos(self, curso, modalidade):
        alunos = self.controladorAluno.getAlunos(curso, modalidade)
        # renderizar a lista de alunos para o usuário

    def get_detalhes_aluno(self, id):
        aluno = self.controladorAluno.getAluno(id)
        # renderizar os detalhes do aluno para o usuário