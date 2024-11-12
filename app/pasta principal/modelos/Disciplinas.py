import requests

class DisciplinaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.matriculas = {}  # Dicionário de matrículas {aluno: [disciplinas]}
        
    def getDisciplinas(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar dados de disciplinas.")
            return []

    def buscarDisciplinaPorId(self, disciplina_id):
        disciplinas = self.getDisciplinas()
        for disciplina in disciplinas:
            if disciplina.get('id') == disciplina_id:
                return disciplina
        return None
    
    def matricularAlunoEmDisciplina(self, aluno_id, disciplina_id):
        if aluno_id not in self.matriculas:
            self.matriculas[aluno_id] = []  # Se não existir, cria uma lista de disciplinas para o aluno
        
        # Verifica se o aluno já está matriculado nesta disciplina
        if disciplina_id not in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].append(disciplina_id)  # Adiciona a disciplina
            return True  # Matrícula realizada com sucesso
        return False  # O aluno já está matriculado na disciplina
    
    def getDisciplinasMatriculadas(self, aluno_id):
        # Retorna as disciplinas matriculadas por um aluno
        if aluno_id in self.matriculas:
            return self.matriculas[aluno_id]
        return []  # Retorna lista vazia se o aluno não estiver matriculado em nenhuma disciplina

    def removerDisciplinaDoAluno(self, aluno_id, disciplina_id):
        if aluno_id in self.matriculas and disciplina_id in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].remove(disciplina_id)
            return True  # Remoção realizada com sucesso
        return False  # O aluno não estava matriculado na disciplina
