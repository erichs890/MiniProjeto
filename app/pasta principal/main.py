from serviços.AlunoServico import AlunoServico
from alunosFiltro import AlunosFiltro
from views.AlunoView import AlunoView

url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"
alunos = AlunoServico(url)
dados = AlunoServico.getAlunos()
filtro = AlunosFiltro()
filtro.filtroHistoria(dados)
view = AlunoView()
view.listar_alunos(filtro)
