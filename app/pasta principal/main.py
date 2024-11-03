from controllers.AlunoController import AlunoController

# URL base do microsserviço de alunos
url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"

controller = AlunoController(url)

controller.listarAlunosHistoria()

# Matricular um aluno em uma disciplina
controller.matricularDisciplina(aluno_id=1, disciplina="História Antiga")

# Listar disciplinas de um aluno
controller.listarDisciplinasMatriculadas(aluno_id=1)

# Remover uma disciplina
controller.removerDisciplina(aluno_id=1, disciplina="História Antiga")
