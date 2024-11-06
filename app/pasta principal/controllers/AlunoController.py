from modelos.Aluno import AlunoModelo
from views.AlunoView import AlunoView

class AlunoController:
    def __init__(self, url):
        self.alunoModelo = AlunoModelo(url)
        self.view = AlunoView()

    def listarAlunosHistoria(self):
        alunosHistoria = self.alunoModelo.filtrarAlunosHistoriaPresencial()
        self.view.listar_alunos(alunosHistoria)

    def buscarAluno(self, id=None, nome=None):
        # Obtém os dados dos alunos
        dados = self.alunoModelo.getAlunos()
        
        # Verifica se os dados foram obtidos corretamente
        if not dados:
            print("Erro: Não foi possível obter os dados dos alunos.")
            return
        
        alunoEncontrado = None
        for aluno in dados:
            # Verifica se estamos buscando por ID ou nome
            if (id and isinstance(id, int) and aluno['id'] == id) or (nome and aluno['nome'].lower() == nome.lower()):
                alunoEncontrado = aluno
                break

        # Exibe as informações do aluno encontrado ou uma mensagem de erro
        if alunoEncontrado:
            self.view.aluno_info(alunoEncontrado)
        else:
            print("Aluno não encontrado. Verifique o ID ou nome fornecido.")