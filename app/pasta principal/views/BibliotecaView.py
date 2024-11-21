class BibliotecaView:
    def listar_livros_disponiveis(self, livros):
        print("\nLivros disponíveis:")
        for livro in livros:
            status = "Reservado" if livro['status'] != "null" else "Disponível"
            print(f"ID: {livro['id']} - Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']} - Status: {status}")
        print()

    def confirmar_reserva(self, livro, nome_aluno):
        print(f"Reserva confirmada: Aluno {nome_aluno} reservou o livro '{livro['titulo']}' com sucesso!")

    def listar_livros_reservados(self, nome_aluno, livros):
        print(f"\nLivros reservados por {nome_aluno}:")
        if livros:
            for livro in livros:
                print(f"- ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Status: {livro['status']}")
        else:
            print("Nenhum livro reservado.")


    def confirmar_reserva(self, livro, nome_aluno):
        if livro:
            print(f"Reserva confirmada: Aluno {nome_aluno} reservou o livro '{livro['titulo']}' com sucesso!")
        else:
            print("Erro: Não foi possível realizar a reserva.")

    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def confirmar_cancelamento(self, nome_aluno, livro):

        if livro:
            print(f"Reserva do livro '{livro['titulo']}' (ID: {livro['id']}) cancelada com sucesso para o aluno {nome_aluno}.")
        else:
            print("Erro: Não foi possível cancelar a reserva. Livro ou aluno não encontrado.")
