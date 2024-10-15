import requests
from serviços.AlunoServico import AlunoServico
url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"
servico = AlunoServico(url)
nome = input("Diz o nome do teu menino: ")
servico.getAlunoPorNome(nome)