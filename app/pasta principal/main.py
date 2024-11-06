from controllers.AlunoController import AlunoController
from controllers.DisciplinaController import DisciplinaController

# URLs dos serviços
aluno_url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"
disciplina_url = "https://sswfuybfs8.execute-api.us-east-2.amazonaws.com/disciplinaServico/msDisciplina"

# Inicializa os controladores
aluno_controller = AlunoController(aluno_url)
disciplina_controller = DisciplinaController(disciplina_url, aluno_controller.alunoModelo)

while True:
    print("\nMenu:")
    print("1. Listar alunos de História na modalidade Presencial")
    print("2. Buscar aluno por ID ou nome")
    print("3. Listar disciplinas disponíveis")
    print("4. Matricular aluno em uma disciplina")
    print("5. Listar disciplinas matriculadas de um aluno")
    print("6. Remover disciplina de um aluno")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        aluno_controller.listarAlunosHistoria()  # Lista os alunos do curso de História na modalidade Presencial
    elif opcao == '2':
        idOuNome = int(input("Digite 1 para buscar por nome, digite 2 para buscar por id: "))
        if idOuNome == 1:
            nome = input("Digite o nome do aluno: ")
            aluno_controller.buscarAluno(nome=nome)  # Busca aluno pelo nome
        elif idOuNome == 2:
            id_aluno = int(input("Digite o ID do aluno: "))
            aluno_controller.buscarAluno(id=id_aluno)  # Busca aluno pelo ID
        else:
            print("Opção inválida")
    elif opcao == '3':
        disciplina_controller.listarDisciplinasDisponiveis()  # Exibe disciplinas disponíveis
    elif opcao == '4':
        aluno_id = int(input("Digite o ID do aluno: "))
        disciplina_id = int(input("Digite o ID da disciplina para matrícula: "))
        disciplina_controller.matricularDisciplina(aluno_id, disciplina_id)  # Matricula o aluno na disciplina
    elif opcao == '5':
        aluno_id = int(input("Digite o ID do aluno: "))
        disciplina_controller.listarDisciplinasMatriculadas(aluno_id)  # Lista as disciplinas matriculadas pelo aluno
    elif opcao == '6':
        aluno_id = int(input("Digite o ID do aluno: "))
        disciplina_id = int(input("Digite o ID da disciplina para remoção: "))
        disciplina_controller.removerDisciplina(aluno_id, disciplina_id)  # Remove a disciplina do aluno
    elif opcao == '0':
        break  # Encerra o programa
    else:
        print("Opção inválida. Tente novamente.")
