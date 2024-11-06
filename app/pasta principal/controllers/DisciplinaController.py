from modelos.Disciplinas import DisciplinaModelo
from views.DisciplinaView import DisciplinaView

class DisciplinaController:
    def __init__(self, disciplina_url, aluno_modelo):
        self.disciplinaModelo = DisciplinaModelo(disciplina_url)
        self.view = DisciplinaView()
        self.alunoModelo = aluno_modelo

    def listarDisciplinasMatriculadas(self, aluno_id):
        aluno = self.alunoModelo.buscarAluno(id=aluno_id)
        if aluno:
            nome_aluno = aluno["nome"]
            disciplina_ids = self.disciplinaModelo.listarDisciplinasAluno(aluno_id)  # Obtém IDs das disciplinas
            disciplinas = []
            for disciplina_id in disciplina_ids:
                disciplina = self.disciplinaModelo.buscarDisciplina(disciplina_id)  # Busca detalhes da disciplina
                if disciplina:
                    disciplinas.append(disciplina)
            self.view.listar_disciplinas_matriculadas(disciplinas, nome_aluno)  # Passa o nome do aluno para a view
        else:
            print("Aluno não encontrado.")

    def matricularDisciplina(self, aluno_id, disciplina_id):
        disciplina = self.disciplinaModelo.buscarDisciplina(disciplina_id)  # Busca a disciplina
        if disciplina:
            self.disciplinaModelo.matricularAluno(aluno_id, disciplina_id)
            self.view.matricula_sucesso(aluno_id, disciplina["nome"])
        else:
            print("Disciplina não encontrada.")

    def removerDisciplina(self, aluno_id, disciplina_id):
        self.disciplinaModelo.removerDisciplina(aluno_id, disciplina_id)
        self.view.remover_disciplina_sucesso(aluno_id, disciplina_id)
