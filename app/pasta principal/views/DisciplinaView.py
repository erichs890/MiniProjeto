class DisciplinaView:
    def listar_disciplinas(self, disciplinas):
        if disciplinas:
            print("Disciplinas disponíveis:")
            for disciplina in disciplinas:
                print(f"ID: {disciplina['id']}, Nome: {disciplina['nome']}")
        else:
            print("Nenhuma disciplina disponível.")

    def listar_disciplinas_matriculadas(self, disciplinas, nome_aluno):
        if disciplinas:
            print(f"Disciplinas matriculadas por {nome_aluno}:")
            for disciplina in disciplinas:
                print(f"ID: {disciplina['id']}, Nome: {disciplina['nome']}")
        else:
            print("Nenhuma disciplina matriculada.")

    def matricula_sucesso(self, aluno_id, disciplina):
        print(f"Aluno {aluno_id} matriculado com sucesso na disciplina: {disciplina}")

    def matricula_falha(self, aluno_id):
        print(f"Falha na matrícula. Verifique se o aluno {aluno_id} está ativo e na modalidade presencial.")

    def remover_disciplina_sucesso(self, aluno_id, disciplina):
        print(f"Disciplina '{disciplina}' removida com sucesso do aluno {aluno_id}.")
