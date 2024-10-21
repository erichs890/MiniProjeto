from controllers.AlunoController import AlunoController

# URL do microsserviço
url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"

# Instanciando o controlador de alunos
aluno_controller = AlunoController(url)

# Chamando a função que lista alunos de História na modalidade presencial
aluno_controller.listar_alunos_historia()
