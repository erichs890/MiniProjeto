import requests

class AlunoModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    def getAlunos(self):
        try:
            response = requests.get(self.urlBase)
            response.raise_for_status()  # Levanta um erro para status HTTP 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados: {e}")
            return []

    def filtrarAlunosHistoriaPresencial(self):
        dados = self.getAlunos()
        
        if not dados:
            print("Erro: Nenhum dado de aluno encontrado.")
            return []
        
        alunosHistoria = [
            aluno for aluno in dados
            if aluno.get('curso') == 'História' and aluno.get('modalidade') == "Presencial"
        ]
        
        return alunosHistoria