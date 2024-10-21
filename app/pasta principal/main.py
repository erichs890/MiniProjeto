from controllers.AlunoController import AlunoController

url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"

aluno_controller = AlunoController(url)

aluno_controller.listar_alunos_historia()
