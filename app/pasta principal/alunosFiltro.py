from serviços.AlunoServicons import AlunoServico
class Filtro:
    def __init__(self, servico_aluno):
        self.servico_aluno = servico_aluno
    
    dados = AlunoServico.getAlunos()

    def filtroHistoria(self, dados,curso, modalidade):
            nomes_historia = []
            for pessoa in dados:
                if 'curso' in pessoa and pessoa['curso'] == curso and 'modalidade' in pessoa and pessoa['modalidade'] == modalidade:
                    if 'nome' in pessoa:
                        nomes_historia.append(pessoa['nome'])
                        contador += 1
                    else:
                        print("Aviso: Encontrado aluno sem nome no JSON.")