from modelos.Biblioteca import BibliotecaModelo
from views.BibliotecaView import BibliotecaView

class BibliotecaController:
    def __init__(self, url, aluno_modelo):
        self.bibliotecaModelo = BibliotecaModelo(url)
        self.alunoModelo = aluno_modelo
        self.view = BibliotecaView()

    def listarLivrosDisponiveis(self):
        livros_disponiveis = self.bibliotecaModelo.getLivros()
        self.view.listar_livros(livros_disponiveis)

    def reservarLivro(self, aluno_id, livro_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        livro = self.bibliotecaModelo.buscarLivroPorId(livro_id)

        if aluno and livro:
            if aluno['status'] == 'Ativo':
                livro_reservado = self.bibliotecaModelo.reservarLivro(aluno_id, livro_id)
                if livro_reservado:
                    self.view.confirmar_reserva(aluno['nome'], livro_reservado)
                else:
                    self.view.exibir_mensagem("O livro já está reservado ou não foi encontrado.")
            else:
                self.view.exibir_mensagem("Apenas alunos ativos podem reservar livros.")
        else:
            self.view.exibir_mensagem("Aluno ou livro não encontrados.")

    def cancelarReserva(self, aluno_id, livro_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        livro = self.bibliotecaModelo.buscarLivroPorId(livro_id)

        if aluno and livro:
            livro_cancelado = self.bibliotecaModelo.cancelarReserva(aluno_id, livro_id)
            if livro_cancelado:
                self.view.confirmar_cancelamento(aluno['nome'], livro_cancelado)
            else:
                self.view.exibir_mensagem("A reserva não foi encontrada para cancelamento.")
        else:
            self.view.exibir_mensagem("Aluno ou livro não encontrados.")

    def listarLivrosReservados(self, aluno_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        if aluno:
            livros_reservados = self.bibliotecaModelo.listarReservas(aluno_id)
            if livros_reservados:
                self.view.listar_livros_reservados(aluno['nome'], livros_reservados)
            else:
                self.view.exibir_mensagem(f"O aluno {aluno['nome']} não tem livros reservados.")
        else:
            self.view.exibir_mensagem("Aluno não encontrado.")
