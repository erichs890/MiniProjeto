class AlunoView:
    def listar_alunos(self, alunos):
        for aluno in alunos:
            print(f"Aluno: {aluno}")
        print(f"{len(alunos)} aluno(s) listado(s)")

    def alunoInfo(self, aluno):
        if aluno:
            print(f"Detalhes do Aluno: {aluno}")
        else:
            print("Aluno não encontrado")

    # Mensagens de matrícula
    def matriculaSucesso(self, aluno_id, disciplina):
        print(f"Aluno {aluno_id} matriculado com sucesso na disciplina: {disciplina}")

    def matriculaFalha(self, aluno_id):
        print(f"Falha na matrícula. Verifique se o aluno {aluno_id} está ativo e na modalidade presencial.")

    def listar_disciplinas(self, disciplinas):
        if disciplinas:
            print("Disciplinas matriculadas:")
            for disciplina in disciplinas:
                print(f" - {disciplina}")
        else:
            print("Nenhuma disciplina matriculada.")

    def removerDisciplinaSucesso(self, aluno_id, disciplina):
        print(f"Disciplina '{disciplina}' removida com sucesso do aluno {aluno_id}.")
