from modelos.Biblioteca import BibliotecaModelo
from views.BibliotecaView import BibliotecaView

class BibliotecaController:
    def __init__(self, url, aluno_modelo):
        self.bibliotecaModelo = BibliotecaModelo(url)
        self.alunoModelo = aluno_modelo
        self.view = BibliotecaView()

    def listarLivrosDisponiveis(self):
        livros = self.bibliotecaModelo.getLivros()
        if livros:
            self.view.listar_livros_disponiveis(livros)
        else:
            self.view.exibir_mensagem("Nenhum livro disponível para reserva.")

    def reservarLivro(self, aluno_id, livro_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        livro = self.bibliotecaModelo.reservarLivro(aluno_id, livro_id)

        if aluno and livro:
            self.view.confirmar_reserva(livro, aluno['nome'])
        elif not aluno:
            print("Erro: Aluno não encontrado.")
        elif not livro:
            print("Erro: Livro não encontrado ou já reservado.")


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


    def cancelarReserva(self, aluno_id, livro_id):
        aluno = self.alunoModelo.buscarAlunoPorId(aluno_id)
        livro = self.bibliotecaModelo.buscarLivroPorId(livro_id)

        if aluno and livro:
            sucesso = self.bibliotecaModelo.cancelarReserva(aluno_id, livro_id)
            if sucesso:
                self.view.confirmar_cancelamento(aluno['nome'], livro)
            else:
                self.view.exibir_mensagem(f"O aluno {aluno['nome']} não tinha reservado o livro '{livro['titulo']}'.")
        else:
            self.view.exibir_mensagem("Aluno ou livro não encontrados.")

