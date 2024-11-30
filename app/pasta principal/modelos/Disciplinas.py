import requests

class DisciplinaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.disciplinas = {}  # Dicionário para armazenar disciplinas {id: disciplina}
        self.matriculas = {}  # Dicionário de matrículas {aluno_id: [disciplinas]}
        self._carregarDisciplinas()

    def _carregarDisciplinas(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            disciplinas = response.json()
            self.disciplinas = {disciplina['id']: disciplina for disciplina in disciplinas}
        else:
            print("Erro ao carregar disciplinas.")

    def getDisciplinas(self):
        return list(self.disciplinas.values())  # Retorna a lista de disciplinas armazenadas

    def buscarDisciplinaPorId(self, disciplina_id):
        return self.disciplinas.get(disciplina_id, None)

    def matricularAlunoEmDisciplina(self, aluno_id, disciplina_id):
        if aluno_id not in self.matriculas:
            self.matriculas[aluno_id] = []  # Cria uma lista de disciplinas para o aluno

        # Verifica se o aluno já está matriculado na disciplina
        if disciplina_id not in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].append(disciplina_id)  # Adiciona a disciplina
            return True  # Matrícula realizada com sucesso
        return False  # O aluno já está matriculado na disciplina

    def getDisciplinasMatriculadas(self, aluno_id):
        if aluno_id in self.matriculas:
            return [self.disciplinas[disciplina_id] for disciplina_id in self.matriculas[aluno_id] if disciplina_id in self.disciplinas]
        return []  # Retorna lista vazia se o aluno não estiver matriculado em nenhuma disciplina

    def removerDisciplinaDoAluno(self, aluno_id, disciplina_id):
        if aluno_id in self.matriculas and disciplina_id in self.matriculas[aluno_id]:
            self.matriculas[aluno_id].remove(disciplina_id)
            return True  # Remoção realizada com sucesso
        return False  # O aluno não estava matriculado na disciplina
