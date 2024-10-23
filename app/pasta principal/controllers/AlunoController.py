from modelos.Aluno import AlunoModelo
from views.AlunoView import AlunoView

class AlunoController:
    def __init__(self, url):
        self.alunoModelo = AlunoModelo(url)
        self.view = AlunoView()

    # Função de filtragem continua no controller
    def filtrarAlunosHistoriaPresencial(self, dados):
        alunosHistoria = []
        for aluno in dados:
            if aluno['curso'] == 'História' and aluno['modalidade'] == "Presencial":
                alunosHistoria.append(aluno['nome'])
        return alunosHistoria

    # Função principal para controlar a exibição dos alunos
    def listarAlunosHistoria(self):
        # Obtém os dados do serviço
        dados = self.alunoModelo.getAlunos()

        # Filtra os alunos de História presencial
        alunosHistoria = self.filtrarAlunosHistoriaPresencial(dados)

        # Passa a lista filtrada para a view exibir
        self.view.listar_alunos(alunosHistoria)

    # Função para buscar aluno por ID ou nome
    def buscarAluno(self, id=None, nome=None):
        # Obtém os dados do serviço
        dados = self.alunoModelo.getAlunos()

        # Verifica se o aluno foi encontrado pelo ID ou nome
        alunoEncontrado = None
        for aluno in dados:
            if (id and isinstance(id, int) and aluno['id'] == id) or (nome and aluno['nome'] == nome):
                alunoEncontrado = aluno
                break

        # Exibe os detalhes do aluno, ou uma mensagem se não encontrado
        self.view.alunoInfo(alunoEncontrado)
