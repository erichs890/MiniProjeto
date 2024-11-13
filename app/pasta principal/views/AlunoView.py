class AlunoView:
    def listar_alunos(self, alunos):
        print("\nAlunos cadastrados:")
        for aluno in alunos:
            print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Curso: {aluno['curso']}, Modalidade: {aluno['modalidade']}, Status: {aluno['status']}")
        print(f"{len(alunos)} aluno(s) listado(s)")

    def aluno_info(self, aluno):
        if aluno:
            print(f"Detalhes do Aluno:\n"
                  f"ID: {aluno['id']}\n"
                  f"Nome: {aluno['nome']}\n"
                  f"Curso: {aluno['curso']}\n"
                  f"Modalidade: {aluno['modalidade']}\n"
                  f"Status: {aluno['status']}")
        else:
            print("Aluno não encontrado")
