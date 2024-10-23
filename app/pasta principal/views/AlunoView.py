# from controllers.AlunoController import AlunoController

class AlunoView:
    # Método responsável por exibir os alunos filtrados
    def listar_alunos(self, alunos_historia):
        contador = 0
        for aluno in alunos_historia:
            print(aluno)
            contador += 1
        print(f"{contador} alunos encontrados.")

    # Método responsável por exibir os detalhes de um aluno específico
    def alunoInfo(self, aluno):
        if aluno:
            print(f"ID: {aluno['id']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Modalidade: {aluno['modalidade']}")
            print(f"Status: {aluno['status']}")
        else:
            print("Aluno não encontrado.")
