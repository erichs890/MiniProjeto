from modelos.Disciplinas import DisciplinaModelo
from views.DisciplinaView import DisciplinaView

class DisciplinaController:
    def __init__(self, url, aluno_modelo):
        self.disciplinaModelo = DisciplinaModelo(url)
        self.alunoModelo = aluno_modelo
        self.view = DisciplinaView()
    def listarDisciplinasDisponiveis(self):
        # Busca todas as disciplinas no modelo e filtra apenas as de História
        todas_disciplinas = self.disciplinaModelo.getDisciplinas()
        disciplinas_historia = [disciplina for disciplina in todas_disciplinas if disciplina.get('curso') == 'História']
        
        # Exibe apenas as disciplinas de História na view
        self.view.listar_disciplinas(disciplinas_historia)


    def matricularDisciplina(self, aluno_id, disciplina_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        disciplina = self.disciplinaModelo.buscarDisciplinaPorId(disciplina_id)

        # Verifica se o aluno está no curso de História e tem status ativo
        if aluno and aluno['curso'] == 'História' and aluno['status'] == 'ativo':
            if disciplina:
                matricula = {'aluno': aluno['nome'], 'disciplina': disciplina['nome']}
                sucesso = self.disciplinaModelo.matricularAlunoEmDisciplina(aluno_id, disciplina_id)

                if sucesso:
                    self.view.exibir_mensagem(f"Aluno {aluno['nome']} foi matriculado na disciplina {disciplina['nome']} com sucesso!")
                else:
                    self.view.exibir_mensagem("Aluno já está matriculado na disciplina.")
            else:
                self.view.exibir_mensagem("Disciplina não encontrada.")
        else:
            self.view.exibir_mensagem("Apenas alunos do curso de História com status ativo podem ser matriculados.")


    def listarDisciplinasMatriculadas(self, aluno_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        if aluno:
            disciplinas_matriculadas_ids = self.disciplinaModelo.getDisciplinasMatriculadas(aluno_id)
            disciplinas_matriculadas = [self.disciplinaModelo.buscarDisciplinaPorId(disc_id) for disc_id in disciplinas_matriculadas_ids]
            if disciplinas_matriculadas:
                self.view.listar_disciplinas_matriculadas(aluno['nome'], disciplinas_matriculadas)
            else:
                self.view.exibir_mensagem(f"O aluno {aluno['nome']} não está matriculado em nenhuma disciplina.")
        else:
            self.view.exibir_mensagem("Aluno não encontrado.")

    def removerDisciplina(self, aluno_id, disciplina_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        disciplina = self.disciplinaModelo.buscarDisciplinaPorId(disciplina_id)

        if aluno and disciplina:
            sucesso = self.disciplinaModelo.removerDisciplinaDoAluno(aluno_id, disciplina_id)
            if sucesso:
                self.view.exibir_mensagem("Disciplina removida com sucesso!")
            else:
                self.view.exibir_mensagem("Aluno não estava matriculado na disciplina.")
        else:
            self.view.exibir_mensagem("Aluno ou disciplina não encontrados.")
