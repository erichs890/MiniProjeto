class AlunoView:
    def listar_alunos(self, alunos):
        print("\nAlunos cadastrados:")
        for aluno in alunos:
            print(f"ID: {aluno['id']}, Nome: {aluno['nome']}")
        print(f"{len(alunos)} aluno(s) listado(s)")

    def aluno_info(self, aluno):
        if aluno:
            print(f"Detalhes do Aluno: {aluno}")
        else:
            print("Aluno não encontrado")
