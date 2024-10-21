from serviços.AlunoServico import AlunoServico
from views.AlunoView import AlunoView

class AlunoController:
    def __init__(self, url):
        self.aluno_servico = AlunoServico(url)
        self.view = AlunoView()

    # Função de filtragem movida para o controller
    def filtrar_alunos_historia_presencial(self, dados):
        alunos_historia = []
        for aluno in dados:
            if aluno['curso'] == 'História' and aluno['modalidade'] == "Presencial":
                alunos_historia.append(aluno['nome'])
        return alunos_historia

    # Função principal para listar alunos de História
    def listar_alunos_historia(self):
        # Obtém os alunos do serviço
        dados = self.aluno_servico.getAlunos()

        # Filtra os alunos de História presencial
        alunos_historia = self.filtrar_alunos_historia_presencial(dados)

        # Passa os alunos filtrados para a view
        self.view.listar_alunos(alunos_historia)
