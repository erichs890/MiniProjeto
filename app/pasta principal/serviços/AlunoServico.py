import requests

class AlunoServico:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    
    def getAlunos(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
                dados = response.json()  # Tenta converter a resposta JSON em um objeto Python
        return dados        










    # def getAlunoPorNome(self, nome_busca):
    #     response = requests.get(self.urlBase)
    #     if response.status_code == 200:
    #         dados = response.json()  
    #         aluno_encontrado = None

    
    #         for pessoa in dados:
    #             if 'nome' in pessoa and pessoa['nome'].lower() == nome_busca.lower():
    #                 aluno_encontrado = pessoa
    #                 break  
            
    #         # Exibe os detalhes do aluno encontrado
    #         if aluno_encontrado:
    #             print(f"Aluno encontrado: {aluno_encontrado['nome']}")
    #             print(f"Curso: {aluno_encontrado['curso']}")
    #             print(f"Modalidade: {aluno_encontrado['modalidade']}")
    #             print(f"Status: {aluno_encontrado['status']}")
    #         else:
    #             print(f"Nenhum aluno encontrado com o nome '{nome_busca}'.")
    #     else:
    #         print(f"Erro na requisição: {response.status_code}")
