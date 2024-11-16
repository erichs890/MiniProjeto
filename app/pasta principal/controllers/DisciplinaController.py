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
            print("\nDisciplinas disponíveis para o curso de História:")
            for disciplina in disciplinas_historia:
                print(f"ID: {disciplina['id']} - Nome: {disciplina['nome']}")
        else:
            print("Não há disciplinas disponíveis para o curso de História.")

    def matricularDisciplina(self, aluno_id, disciplina_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        disciplina = self.disciplinaModelo.buscarDisciplinaPorId(disciplina_id)

        # Depuração: Verifique e exiba os dados do aluno para confirmar que estamos recebendo o curso, modalidade e status corretos
        print("Depuração - Dados do Aluno:")
        print(aluno)  # Mostra todos os dados do aluno

        # Verifica se o aluno é do curso de História, modalidade presencial, e está ativo
        if aluno:
            curso_aluno = aluno.get('curso')
            modalidade = aluno.get('modalidade')
            status = aluno.get('status')

            # Exibe o curso, modalidade e status do aluno
            print(f"Curso: {curso_aluno}, Modalidade: {modalidade}, Status: {status}")

            # Verificar se o aluno é do curso de História
            if curso_aluno == 'História' and modalidade == "Presencial" and status == 'Ativo':
                if disciplina:
                    curso_disciplina = disciplina.get('curso')  # Verifica o curso da disciplina

                    # Verificar se a disciplina é do curso de História
                    if curso_disciplina == 'História':
                        sucesso = self.disciplinaModelo.matricularAlunoEmDisciplina(aluno_id, disciplina_id)
                        if sucesso:
                            self.view.exibir_mensagem(f"Aluno {aluno['nome']} foi matriculado na disciplina {disciplina['nome']} com sucesso!")
                        else:
                            self.view.exibir_mensagem("Aluno já está matriculado na disciplina.")
                    else:
                        self.view.exibir_mensagem("A disciplina não é do curso de História.")
                else:
                    self.view.exibir_mensagem("Disciplina não encontrada.")
            else:
                self.view.exibir_mensagem("Apenas alunos do curso de História com status ativo podem ser matriculados.")
        else:
            self.view.exibir_mensagem("Aluno não encontrado.")

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
