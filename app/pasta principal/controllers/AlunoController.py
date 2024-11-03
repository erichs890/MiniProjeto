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

        self.view.alunoInfo(alunoEncontrado)
 
        # Funcionalidades de matrícula em disciplinas

    # Matricula um aluno em uma disciplina
    def matricularDisciplina(self, aluno_id, disciplina):
        aluno = next((aluno for aluno in self.alunoModelo.getAlunos() if aluno['id'] == aluno_id and aluno['status'] == 'Ativo' and aluno['modalidade'] == 'Presencial'), None)
        if aluno:
            self.alunoModelo.matricularDisciplina(aluno_id, disciplina)
            self.view.matriculaSucesso(aluno_id, disciplina)
        else:
            self.view.matriculaFalha(aluno_id)

    # Lista disciplinas em que o aluno está matriculado
    def listarDisciplinasMatriculadas(self, aluno_id):
        disciplinas = self.alunoModelo.listarDisciplinasMatriculadas(aluno_id)
        self.view.listar_disciplinas(disciplinas)

    # Remove uma disciplina da matrícula do aluno
    def removerDisciplina(self, aluno_id, disciplina):
        self.alunoModelo.removerDisciplina(aluno_id, disciplina)
        self.view.removerDisciplinaSucesso(aluno_id, disciplina)