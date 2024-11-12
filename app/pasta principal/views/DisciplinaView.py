class DisciplinaView:
    def listar_disciplinas(self, disciplinas):
        for disciplina in disciplinas:
            print(f"ID: {disciplina['id']}, Nome: {disciplina['nome']}")

    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def listar_disciplinas_matriculadas(self, nome_aluno, disciplinas):
        print(f"\nDisciplinas em que {nome_aluno} está matriculado:")
        for disciplina in disciplinas:
            print(f"- {disciplina['nome']} (ID: {disciplina['id']})")