import requests

class BibliotecaModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase
        self.reservas = {}  # Dicionário para armazenar reservas {aluno_id: [livros_reservados]}

    def getLivros(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            livros = response.json()
            # Atualiza o status dos livros com base nas reservas
            for livro in livros:
                for aluno_id, livros_reservados in self.reservas.items():
                    if livro['id'] in livros_reservados:
                        livro['status'] = 'Reservado'
            return livros
        else:
            print("Erro ao buscar dados da biblioteca.")
            return []

    def buscarLivroPorId(self, livro_id):
        livros = self.getLivros()
        for livro in livros:
            if livro.get('id') == livro_id:
                return livro
        return None

    def reservarLivro(self, aluno_id, livro_id):
        livros = self.getLivros()
        livro = next((l for l in livros if l['id'] == livro_id), None)
        
        if livro:
            if aluno_id not in self.reservas:
                self.reservas[aluno_id] = []  # Cria uma lista de reservas para o aluno, se não existir
            
            if livro_id not in self.reservas[aluno_id]:
                self.reservas[aluno_id].append(livro_id)  # Adiciona o livro às reservas do aluno
                livro['status'] = 'Reservado'  # Atualiza o status do livro
                return livro  # Retorna o objeto do livro reservado
            else:
                print(f"O aluno {aluno_id} já reservou o livro '{livro['titulo']}'.")
        else:
            print("Erro: Livro não encontrado.")
        
        return None  # Retorna None se o livro não foi reservado

    def cancelarReserva(self, aluno_id, livro_id):
        if aluno_id in self.reservas and livro_id in self.reservas[aluno_id]:
            self.reservas[aluno_id].remove(livro_id)
            livros = self.getLivros()
            livro = next((l for l in livros if l['id'] == livro_id), None)
            if livro:
                livro['status'] = 'null'  # Atualiza o status localmente
            return livro  # Retorna o livro cujo status foi atualizado
        return None  # Retorna None se a reserva não foi encontrada


    def listarReservas(self, aluno_id):
        if aluno_id in self.reservas:
            livros_reservados_ids = self.reservas[aluno_id]
            livros = self.getLivros()
            # Filtra os livros cujo ID está na lista de reservas do aluno
            return [livro for livro in livros if livro['id'] in livros_reservados_ids]
        return []  # Retorna uma lista vazia se o aluno não tiver reservas
