from modelos.Aluno import AlunoModelo
from views.AlunoView import AlunoView

class AlunoController:
    def __init__(self, url):
        self.alunoModelo = AlunoModelo(url)
        self.view = AlunoView()

    def listarAlunosHistoria(self):
        alunosHistoria = self.alunoModelo.filtrarAlunosHistoriaPresencial()
        self.view.listar_alunos(alunosHistoria)

    def buscarAluno(self, id=None, nome=None):
        dados = self.alunoModelo.getAlunos()
        alunoEncontrado = None
        for aluno in dados:
            if (id and isinstance(id, int) and aluno['id'] == id) or (nome and aluno['nome'] == nome):
                alunoEncontrado = aluno
                break
        self.view.aluno_info(alunoEncontrado)
