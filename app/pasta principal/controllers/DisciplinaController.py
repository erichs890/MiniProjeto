from modelos.Disciplinas import DisciplinaModelo
from views.DisciplinaView import DisciplinaView

class DisciplinaController:
    def __init__(self, url, aluno_modelo):
        self.disciplinaModelo = DisciplinaModelo(url)
        self.alunoModelo = aluno_modelo
        self.view = DisciplinaView()

    def listarDisciplinasDisponiveis(self):
        disciplinas = self.disciplinaModelo.getDisciplinas()  # Obtém todas as disciplinas
        disciplinas_historia = [d for d in disciplinas if d['curso'] == 'História']  # Filtra as disciplinas do curso de História
        
        if disciplinas_historia:
            self.view.listar_disciplinas(disciplinas_historia)
        else:
            self.view.exibir_mensagem("Não há disciplinas disponíveis para o curso de História.")

    def matricularDisciplina(self, aluno_id, disciplina_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        disciplina = self.disciplinaModelo.buscarDisciplinaPorId(disciplina_id)

        if aluno:
            curso_aluno = aluno.get('curso')
            modalidade = aluno.get('modalidade')
            status = aluno.get('status')

            if curso_aluno == 'História' and modalidade == "Presencial" and status == 'Ativo':
                if disciplina and disciplina.get('curso') == 'História':
                    sucesso = self.disciplinaModelo.matricularAlunoEmDisciplina(aluno_id, disciplina_id)
                    if sucesso:
                        self.view.exibir_mensagem(f"Aluno {aluno['nome']} foi matriculado na disciplina {disciplina['nome']} com sucesso!")
                    else:
                        self.view.exibir_mensagem("Aluno já está matriculado na disciplina.")
                else:
                    self.view.exibir_mensagem("Disciplina não encontrada ou não pertence ao curso de História.")
            else:
                self.view.exibir_mensagem("Apenas alunos do curso de História com status ativo podem ser matriculados.")
        else:
            self.view.exibir_mensagem("Aluno não encontrado.")

    def listarDisciplinasMatriculadas(self, aluno_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        if aluno:
            disciplinas_matriculadas = self.disciplinaModelo.getDisciplinasMatriculadas(aluno_id)
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
