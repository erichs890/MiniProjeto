import requests

class AlunoModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.alunos = self._carregarAlunos()  # Consome a API apenas uma vez

    def _carregarAlunos(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            dados = response.json()
            return tuple(dados)  # Armazena os dados como uma tupla
        else:
            print("Erro ao buscar dados")
            return ()

    def buscarAlunoPorId(self, id_aluno):

        for aluno in self.alunos:
            if aluno.get('id') == id_aluno:
                return aluno
        return None

    def filtrarAlunosHistoriaPresencial(self):
        return [
            aluno for aluno in self.alunos
            if aluno.get('curso') == 'História' and aluno.get('modalidade') == "Presencial"
        ]
