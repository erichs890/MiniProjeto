import requests

class BibliotecaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.reservas = {}  # Dicionário para armazenar reservas: {aluno_id: [livro_id, ...]}

    def getLivros(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar livros da biblioteca.")
            return []
    def reservarLivro(self, aluno_id, livro_id):
        livros_disponiveis = self.getLivros()
        livro = next((l for l in livros_disponiveis if l['id'] == livro_id), None)
        
        if livro and livro['status'] == "null":
            if aluno_id not in self.reservas:
                self.reservas[aluno_id] = []
            self.reservas[aluno_id].append(livro_id)
            livro['status'] = 'Reservado'  # Atualiza o status localmente
            return livro  # Retorna o livro reservado
        elif livro:
            return None  # Retorna None se o livro já estiver reservado
        else:
            return None  # Retorna None se o livro não for encontrado

    def listarReservas(self, aluno_id):
        livros_reservados = self.reservas.get(aluno_id, [])
        livros_disponiveis = self.getLivros()
        return [l for l in livros_disponiveis if l['id'] in livros_reservados]

    def cancelarReserva(self, aluno_id, livro_id):
        if aluno_id in self.reservas and livro_id in self.reservas[aluno_id]:
            self.reservas[aluno_id].remove(livro_id)
            return f"Reserva do livro com ID {livro_id} cancelada com sucesso."
        return "Reserva não encontrada."
