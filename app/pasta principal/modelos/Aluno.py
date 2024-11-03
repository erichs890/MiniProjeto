import requests

class AlunoModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.matriculas = {} 
        
    def getAlunos(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar dados")
            return []

    def filtrarAlunosHistoriaPresencial(self):
        # Obtém todos os alunos
        dados = self.getAlunos()

        # Filtra os alunos de História na modalidade presencial
        alunosHistoria = [
            aluno for aluno in dados
            if aluno.get('curso') == 'História' and aluno.get('modalidade') == "Presencial"
        ]
        
        return alunosHistoria
    
    # Métodos para manipulação de matrículas

    # Adiciona uma disciplina para o aluno se ele estiver apto
    def matricularDisciplina(self, aluno_id, disciplina):
        if aluno_id not in self.matriculas:
            self.matriculas[aluno_id] = []

        self.matriculas[aluno_id].append(disciplina)

    # Lista disciplinas em que um aluno está matriculado
    def listarDisciplinasMatriculadas(self, aluno_id):
        return self.matriculas.get(aluno_id, [])

    # Remove uma disciplina da matrícula do aluno
    def removerDisciplina(self, aluno_id, disciplina):
        if aluno_id in self.matriculas and disciplina in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].remove(disciplina)