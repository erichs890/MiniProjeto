from modelos.Disciplinas import DisciplinaModelo
from views.DisciplinaView import DisciplinaView

class DiciplinaController:
    def __init__(self, disciplina_url, aluno_modelo):
        self.disciplinaModelo = DisciplinaModelo(disciplina_url)
        self.view = DisciplinaView()
        self.alunoModelo = aluno_modelo  # Recebe o modelo de alunos para verificar status

    def matricularDisciplina(self, aluno_id):
        # Exibir disciplinas disponíveis
        print("Disciplinas Disponíveis:")
        for disciplina in self.disciplinaModelo.getDisciplinas():  # Supondo que você tenha esse método
            print(f"ID: {disciplina['id']}, Curso: {disciplina['curso']}, Nome: {disciplina['nome']}")

        matricula_tipo = input("Você deseja matricular-se pelo ID da disciplina (digite 'id') ou pelo nome da disciplina (digite 'nome')? ")

        if matricula_tipo == 'id':
            disciplina_id = int(input("Digite o ID da disciplina que deseja se matricular: "))
            # Adicionar lógica para verificar se a disciplina existe e matricular
            self.disciplinaModelo.matricularDisciplina(aluno_id, disciplina_id)
            self.view.matriculaSucesso(aluno_id, disciplina_id)
        elif matricula_tipo == 'nome':
            disciplina_nome = input("Digite o nome da disciplina que deseja se matricular: ")
            # Adicionar lógica para verificar se a disciplina existe e matricular
            self.disciplinaModelo.matricularDisciplinaPorNome(aluno_id, disciplina_nome)
            self.view.matriculaSucesso(aluno_id, disciplina_nome)
        else:
            print("Opção inválida.")


    def listarDisciplinasMatriculadas(self, aluno_id):
        disciplinas = self.disciplinaModelo.listarDisciplinasMatriculadas(aluno_id)
        self.view.listar_disciplinas(disciplinas)

    def removerDisciplina(self, aluno_id, disciplina):
        self.disciplinaModelo.removerDisciplina(aluno_id, disciplina)
        self.view.removerDisciplinaSucesso(aluno_id, disciplina)
