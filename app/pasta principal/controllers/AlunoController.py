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
        """
        Busca um aluno por ID ou nome.
        """
        alunoEncontrado = None

        # Busca por ID
        if id:
            alunoEncontrado = self.alunoModelo.buscarAlunoPorId(id)
        
        # Busca por nome
        elif nome:
            for aluno in self.alunoModelo.alunos:
                if aluno['nome'].lower() == nome.lower():
                    alunoEncontrado = aluno
                    break

        # Exibe as informações do aluno encontrado ou uma mensagem de erro
        if alunoEncontrado:
            self.view.aluno_info(alunoEncontrado)
        else:
            print("Aluno não encontrado. Verifique o ID ou nome fornecido.")
