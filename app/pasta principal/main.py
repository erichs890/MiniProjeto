from controllers.AlunoController import AlunoController

url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"
controller = AlunoController(url)

controller.listarAlunosHistoria()

# Buscar aluno por ID ou nome
controller.buscarAluno(id=123)  # Exemplo de busca por ID
controller.buscarAluno(nome="João")  # Exemplo de busca por nome
