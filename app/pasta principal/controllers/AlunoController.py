from modelos.Aluno import AlunoModelo
from views.AlunoView import AlunoView

class AlunoController:
    def __init__(self, url):
        # Inicializa o modelo e a view
        self.alunoModelo = AlunoModelo(url)
        self.view = AlunoView()

    def listarAlunosHistoria(self):
        # Filtra os alunos diretamente pelo modelo
        alunosHistoria = self.alunoModelo.filtrarAlunosHistoriaPresencial()
        
        # Passa a lista filtrada para a view exibir
        self.view.listar_alunos(alunosHistoria)

    def buscarAluno(self, id=None, nome=None):
        # Obtém todos os alunos do modelo
        dados = self.alunoModelo.getAlunos()

        # Verifica se o aluno foi encontrado pelo ID ou nome
        alunoEncontrado = None
        for aluno in dados:
            if (id and isinstance(id, int) and aluno['id'] == id) or (nome and aluno['nome'] == nome):
                alunoEncontrado = aluno
                break

        # Exibe os detalhes do aluno ou uma mensagem de não encontrado
        self.view.alunoInfo(alunoEncontrado)
