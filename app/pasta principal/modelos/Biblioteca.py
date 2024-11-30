import requests

class BibliotecaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.livros = {}  # Dicionário para armazenar livros {id: livro}
        self.reservas = {}  # Dicionário para armazenar reservas {aluno_id: [livros_reservados]}
        self._carregarLivros()

    def _carregarLivros(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            livros = response.json()
            self.livros = {livro['id']: livro for livro in livros}  # Converte para dicionário
        else:
            print("Erro ao carregar livros da biblioteca.")

    def getLivros(self):
        for livro_id, livro in self.livros.items():
            livro['status'] = "Reservado" if any(livro_id in reservas for reservas in self.reservas.values()) else "Disponível"
        return self.livros

    def buscarLivroPorId(self, livro_id):
        return self.livros.get(livro_id, None)

    def reservarLivro(self, aluno_id, livro_id):
        livro = self.buscarLivroPorId(livro_id)
        if livro and livro['status'] == "Disponível":
            if aluno_id not in self.reservas:
                self.reservas[aluno_id] = []  # Cria a lista de reservas para o aluno, se não existir
            self.reservas[aluno_id].append(livro_id)  # Adiciona o ID do livro à lista de reservas
            livro['status'] = "Reservado"  # Atualiza o status localmente
            return livro  # Retorna o livro reservado
        return None  # Retorna None se o livro já está reservado ou não existe

    def cancelarReserva(self, aluno_id, livro_id):
        if aluno_id in self.reservas and livro_id in self.reservas[aluno_id]:
            self.reservas[aluno_id].remove(livro_id)
            if not self.reservas[aluno_id]:  # Remove o aluno se não tiver mais reservas
                del self.reservas[aluno_id]
            livro = self.buscarLivroPorId(livro_id)
            if livro:
                livro['status'] = "Disponível"
            return livro  # Retorna o livro cujo status foi atualizado
        return None  # Retorna None se a reserva não foi encontrada

    def listarReservas(self, aluno_id):
        if aluno_id in self.reservas:
            livros_reservados_ids = self.reservas[aluno_id]
            return [self.buscarLivroPorId(livro_id) for livro_id in livros_reservados_ids if livro_id in self.livros]
        return []
