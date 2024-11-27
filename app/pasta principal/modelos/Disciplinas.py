import requests

class DisciplinaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.disciplinas = self._carregarDisciplinas()  # Consome a API uma vez
        self.matriculas = {}  # Dicionário de matrículas {aluno: [disciplinas]}

    def _carregarDisciplinas(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            dados = response.json()
            return tuple(dados)  # Armazena os dados como uma tupla
        else:
            print("Erro ao buscar dados de disciplinas.")
            return ()

    def buscarDisciplinaPorId(self, disciplina_id):
        for disciplina in self.disciplinas:
            if disciplina.get('id') == disciplina_id:
                return disciplina
        return None

    def matricularAlunoEmDisciplina(self, aluno_id, disciplina_id):
        if aluno_id not in self.matriculas:
            self.matriculas[aluno_id] = []  # Cria uma lista de disciplinas para o aluno, se não existir
        
        # Verifica se o aluno já está matriculado na disciplina
        if disciplina_id not in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].append(disciplina_id)  # Adiciona a disciplina
            return True  # Matrícula realizada com sucesso
        return False  # O aluno já está matriculado na disciplina

    def getDisciplinasMatriculadas(self, aluno_id):
        if aluno_id in self.matriculas:
            return self.matriculas[aluno_id]
        return []  # Retorna lista vazia se o aluno não estiver matriculado em nenhuma disciplina

    def removerDisciplinaDoAluno(self, aluno_id, disciplina_id):
        if aluno_id in self.matriculas and disciplina_id in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].remove(disciplina_id)
            return True  # Remoção realizada com sucesso
        return False  # O aluno não estava matriculado na disciplina
