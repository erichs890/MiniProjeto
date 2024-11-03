import requests

class DisciplinaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.matriculas = {}  # Armazena matrículas em memória, associando alunos às disciplinas

    def getDisciplinas(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar disciplinas")
            return []
    
    def matricularAluno(self, aluno_id, disciplina_id):
        # Adiciona disciplina à lista de matrículas do aluno
        if aluno_id in self.matriculas:
            self.matriculas[aluno_id].add(disciplina_id)
        else:
            self.matriculas[aluno_id] = {disciplina_id}

    def listarDisciplinasAluno(self, aluno_id):
        # Retorna disciplinas matriculadas para o aluno
        return self.matriculas.get(aluno_id, set())

    def removerDisciplina(self, aluno_id, disciplina_id):
        # Remove uma disciplina da lista de matrículas do aluno
        if aluno_id in self.matriculas:
            self.matriculas[aluno_id].discard(disciplina_id)
