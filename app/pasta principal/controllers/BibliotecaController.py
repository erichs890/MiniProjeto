from modelos.Biblioteca import BibliotecaModelo
from views.BibliotecaView import BibliotecaView

class BibliotecaController:
    def __init__(self, url, biblioteca_model=None):
        # Inicializa o modelo e a view
        self.biblioteca_model = biblioteca_model or BibliotecaModelo(url)
        self.biblioteca_view = BibliotecaView()
        self.reservas = []  # Armazena as reservas em memória

    def listarLivrosDisponiveis(self):
        """
        Obtém os livros disponíveis e exibe na view.
        """
        livros_disponiveis = self.biblioteca_model.getLivros()
        self.biblioteca_view.listar_livros_disponiveis(livros_disponiveis)

    def reservarLivro(self, aluno, livro_id):
        """
        Tenta reservar um livro para o aluno, verificando seu status.
        """
        # Verifica se o aluno está ativo antes de tentar reservar o livro
        if aluno['status'] != "Ativo":
            print("Erro: Apenas alunos ativos podem reservar livros.")
            return

        # Tenta reservar o livro através do modelo
        livro_reservado = self.biblioteca_model.reservarLivro(aluno['id'], livro_id)
        
        if livro_reservado:
            # Caso a reserva seja bem-sucedida, armazena a reserva em memória
            self.reservas.append({'aluno_id': aluno['id'], 'livro_id': livro_reservado['id'], 'titulo': livro_reservado['titulo']})
            self.biblioteca_view.confirmar_reserva(livro_reservado)  # Chama a view para confirmar a reserva
        else:
            self.biblioteca_view.confirmar_reserva(None)  # Chama a view se a reserva falhar

    def listarReservas(self, aluno_id):
        """
        Exibe as reservas de livros de um aluno, baseado no seu ID.
        """
        # Filtra as reservas do aluno pelo ID
        reservas_aluno = [reserva for reserva in self.reservas if reserva['aluno_id'] == aluno_id]
        self.biblioteca_view.listar_reservas(reservas_aluno)

    def cancelarReserva(self, aluno_id, livro_id):
        """
        Cancela a reserva de um livro para um aluno, se ele tiver reservado.
        """
        # Verifica se o aluno tem a reserva do livro
        reserva = next((reserva for reserva in self.reservas if reserva['aluno_id'] == aluno_id and reserva['livro_id'] == livro_id), None)

        if reserva:
            # Remove a reserva da lista
            self.reservas.remove(reserva)
            # Atualiza o status do livro para disponível
            self.biblioteca_model.cancelarReserva(aluno_id, livro_id)
            self.biblioteca_view.confirmar_cancelamento(reserva)  # Confirma o cancelamento na view
        else:
            print("Reserva não encontrada para o aluno e livro especificados.")
