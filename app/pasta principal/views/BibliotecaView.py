class BibliotecaView:
    def listar_livros(self, livros):
        print("\nLivros disponíveis:")
        for livro_id, livro in livros.items():
            print(f"ID: {livro_id}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Status: {livro['status']}")
        print()

    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def listar_livros_reservados(self, aluno_nome, livros_reservados):
        print(f"\nLivros reservados por {aluno_nome}:")
        for livro in livros_reservados:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        print()

    def confirmar_reserva(self, aluno_nome, livro):
        print(f"Reserva confirmada: Aluno {aluno_nome} reservou o livro '{livro['titulo']}' com sucesso!")

    def confirmar_cancelamento(self, aluno_nome, livro):
        print(f"Reserva do livro '{livro['titulo']}' para o aluno {aluno_nome} foi cancelada com sucesso.")
