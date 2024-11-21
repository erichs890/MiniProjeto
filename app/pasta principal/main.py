from controllers.AlunoController import AlunoController
from controllers.DisciplinaController import DisciplinaController
from controllers.BibliotecaController import BibliotecaController

# URLs dos serviços
aluno_url = "https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno"
disciplina_url = "https://sswfuybfs8.execute-api.us-east-2.amazonaws.com/disciplinaServico/msDisciplina"
biblioteca_url = "https://qiiw8bgxka.execute-api.us-east-2.amazonaws.com/acervo/biblioteca"

# Inicializa os controladores
aluno_controller = AlunoController(aluno_url)
disciplina_controller = DisciplinaController(disciplina_url, aluno_controller.alunoModelo)
biblioteca_controller = BibliotecaController(biblioteca_url, aluno_controller.alunoModelo)

while True:
    print("\nMenu Principal:")
    print("1. Alunos")
    print("2. Disciplinas")
    print("3. Biblioteca")
    print("0. Sair")

    opcao_principal = input("Escolha uma opção: ")

    if opcao_principal == '1':
        print("\nMenu de Alunos:")
        print("1. Listar alunos de História na modalidade Presencial")
        print("2. Buscar aluno por ID ou nome")
        opcao_aluno = input("Escolha uma opção: ")
        
        if opcao_aluno == '1':
            aluno_controller.listarAlunosHistoria()
        elif opcao_aluno == '2':
            idOuNome = int(input("Digite 1 para buscar por nome, digite 2 para buscar por id: "))
            if idOuNome == 1:
                nome = input("Digite o nome do aluno: ")
                aluno_controller.buscarAluno(nome=nome)
            elif idOuNome == 2:
                id_aluno = int(input("Digite o ID do aluno: "))
                aluno_controller.buscarAluno(id=id_aluno)
            else:
                print("Opção inválida.")
        else:
            print("Opção inválida.")

    elif opcao_principal == '2':
        print("\nMenu de Disciplinas:")
        print("1. Listar disciplinas disponíveis")
        print("2. Matricular aluno em uma disciplina")
        print("3. Listar disciplinas matriculadas de um aluno")
        print("4. Remover disciplina de um aluno")
        opcao_disciplina = input("Escolha uma opção: ")

        if opcao_disciplina == '1':
            disciplina_controller.listarDisciplinasDisponiveis()
        elif opcao_disciplina == '2':
            aluno_id = int(input("Digite o ID do aluno: "))
            disciplina_id = int(input("Digite o ID da disciplina para matrícula: "))
            disciplina_controller.matricularDisciplina(aluno_id, disciplina_id)
        elif opcao_disciplina == '3':
            aluno_id = int(input("Digite o ID do aluno: "))
            disciplina_controller.listarDisciplinasMatriculadas(aluno_id)
        elif opcao_disciplina == '4':
            aluno_id = int(input("Digite o ID do aluno: "))
            disciplina_id = int(input("Digite o ID da disciplina para remoção: "))
            disciplina_controller.removerDisciplina(aluno_id, disciplina_id)
        else:
            print("Opção inválida.")

    elif opcao_principal == '3':
        print("\nMenu de Biblioteca:")
        print("1. Listar livros disponíveis")
        print("2. Reservar livro")
        print("3. Listar livros reservados")
        print("4. Cancelar reserva de livro")
        opcao_biblioteca = input("Escolha uma opção: ")

        if opcao_biblioteca == '1':
            biblioteca_controller.listarLivrosDisponiveis()
        elif opcao_biblioteca == '2':
            aluno_id = int(input("Digite o ID do aluno: "))
            livro_id = int(input("Digite o ID do livro para reservar: "))
            biblioteca_controller.reservarLivro(aluno_id, livro_id)
        elif opcao_biblioteca == '3':
            aluno_id = int(input("Digite o ID do aluno: "))
            biblioteca_controller.listarLivrosReservados(aluno_id)
        elif opcao_biblioteca == '4':
            aluno_id = int(input("Digite o ID do aluno: "))
            livro_id = int(input("Digite o ID do livro para cancelar reserva: "))
            biblioteca_controller.cancelarReserva(aluno_id, livro_id)
        else:
            print("Opção inválida.")

    elif opcao_principal == '0':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
