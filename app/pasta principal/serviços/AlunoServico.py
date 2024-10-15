import requests

class AlunoServico:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    #Função para verificar quais e quantos alunos estão em determinada diciplina e modalidade
    def getAlunosDiciplina(self, curso, modalidade):
        response = requests.get(self.urlBase)
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

    def getAlunoPorNome(self, nome_busca):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            dados = response.json()  
            aluno_encontrado = None

    
            for pessoa in dados:
                if 'nome' in pessoa and pessoa['nome'].lower() == nome_busca.lower():
                    aluno_encontrado = pessoa
                    break  
            
            # Exibe os detalhes do aluno encontrado
            if aluno_encontrado:
                print(f"Aluno encontrado: {aluno_encontrado['nome']}")
                print(f"Curso: {aluno_encontrado['curso']}")
                print(f"Modalidade: {aluno_encontrado['modalidade']}")
                print(f"Status: {aluno_encontrado['status']}")
            else:
                print(f"Nenhum aluno encontrado com o nome '{nome_busca}'.")
        else:
            print(f"Erro na requisição: {response.status_code}")
