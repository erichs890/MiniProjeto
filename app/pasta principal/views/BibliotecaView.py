class BibliotecaView:
    def listar_livros_disponiveis(self, livros):
        print("\nLivros disponíveis:")
        if not livros:
            print("Nenhum livro disponível no momento.")
        else:
            for livro in livros:
                print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        print()

    def confirmar_reserva(self, livro):
        if livro:
            print(f"Livro reservado com sucesso: {livro['titulo']} - {livro['autor']}")
        else:
            print("Erro: Não foi possível reservar o livro ou o livro já está reservado.")


    def listar_reservas(self, reservas):
        print("\nLivros reservados:")
        if not reservas:
            print("Nenhuma reserva encontrada.")
        else:
            for reserva in reservas:
                print(f"ID: {reserva['id']}, Título: {reserva['titulo']}, Autor: {reserva['autor']}, Ano: {reserva['ano']}")
        print()

    def confirmar_cancelamento(self, livro):
        if livro:
            print(f"Reserva do livro '{livro['titulo']}' cancelada com sucesso.")
        else:
            print("Erro: Não foi possível cancelar a reserva.")
