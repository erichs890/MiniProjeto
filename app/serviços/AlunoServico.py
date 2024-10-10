import requests
# url = 'https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno'

class AlunoServico:
    def __init__(self, url_base):
        self.url_base = url_base

    #Função para verificar quais e quantos alunos estão em determinada diciplina e modalidade
    def getAlunos(self, curso, modalidade):
        response = requests.get(self.url_base)
        contador = 0
        if response.status_code == 200:
                dados = response.json()  # Tenta converter a resposta JSON em um objeto Python
                nomes_historia = []
                for pessoa in dados:
                        # Verifica se a chave 'curso' existe e se o valor é 'História'
                        if 'curso' in pessoa and pessoa['curso'] == curso and 'modalidade' in pessoa and pessoa['modalidade'] == modalidade:
                            # Verifica se a chave 'nome' existe para adicionar à lista
                            if 'nome' in pessoa:
                                nomes_historia.append(pessoa['nome'])
                                contador += 1
                            else:
                                print("Aviso: Encontrado aluno sem nome no JSON.")
                    
                print("Alunos que fazem História presencialmente:")
                for nome in nomes_historia:
                    print(nome)
                print(f"{contador} pessoas")
