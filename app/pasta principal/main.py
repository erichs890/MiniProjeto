from controllers.AlunoController import AlunoController

# URL do microsserviço
url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"

# Instanciando o controlador de alunos
aluno_controller = AlunoController(url)


# Exemplo de busca por ID ou nome
aluno_controller.buscarAluno(id=1)  # Busca por ID

