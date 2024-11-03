# main.py

from controllers.AlunoController import AlunoController
from controllers.DiciplinaController import DiciplinaController

aluno_url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno" 
disciplina_url = "https://sswfuybfs8.execute-api.us-east-2.amazonaws.com/disciplinaServico/msDisciplina" 

aluno_controller = AlunoController(aluno_url)
disciplina_controller = DiciplinaController(disciplina_url, aluno_controller.alunoModelo)

while True:
    print("Menu:")
    print("1. Listar alunos de História na modalidade Presencial")
    print("2. Buscar aluno por ID ou nome")
    print("3. Matricular aluno em uma disciplina")
    print("4. Listar disciplinas matriculadas de um aluno")
    print("5. Remover disciplina de um aluno")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        aluno_controller.listarAlunosHistoria()
    elif opcao == '2':
        idOuNome = int(input("Digite 1 para buscar por nome, digite 2 para buscar por id: "))
        if idOuNome == 1:
            nome = input("Digite o nome do aluno: ")
            aluno_controller.buscarAluno(nome=nome)  # Usando a função existente
        elif idOuNome == 2:
            id_aluno = int(input("Digite o ID do aluno: "))
            aluno_controller.buscarAluno(id=id_aluno)  # Usando a função existente
        else:
            print("Opção inválida")
    elif opcao == '3':
        aluno_id = int(input("Digite o ID do aluno: "))
        disciplina = input("Digite o nome da disciplina: ")
        disciplina_controller.matricularDisciplina(aluno_id, disciplina)
    elif opcao == '4':
        aluno_id = int(input("Digite o ID do aluno: "))
        disciplina_controller.listarDisciplinasMatriculadas(aluno_id)
    elif opcao == '5':
        aluno_id = int(input("Digite o ID do aluno: "))
        disciplina = input("Digite o nome da disciplina: ")
        disciplina_controller.removerDisciplina(aluno_id, disciplina)
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")
