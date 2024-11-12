# modelos/Aluno.py

import requests

class AlunoModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    def getAlunos(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar dados")
            return []

    def buscarAlunoPorId(self, id_aluno):
        # Busca todos os alunos e retorna o que possui o ID especificado
        alunos = self.getAlunos()
        for aluno in alunos:
            if aluno.get('id') == id_aluno:
                return aluno
        return None

    def filtrarAlunosHistoriaPresencial(self):
        # Obtém todos os alunos
        dados = self.getAlunos()

        # Filtra os alunos de História na modalidade presencial
        alunosHistoria = [
            aluno for aluno in dados
            if aluno.get('curso') == 'História' and aluno.get('modalidade') == "Presencial"
        ]
        
        return alunosHistoria
