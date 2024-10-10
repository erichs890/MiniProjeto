import requests

url = 'https://rmi6vdpsq8.execute-api.us-east-2.amazonaws.com/msAluno'

response = requests.get(url)
contador = 0

if response.status_code == 200:
        dados = response.json()  # Tenta converter a resposta JSON em um objeto Python
        nomes_historia = []

        for pessoa in dados:
                # Verifica se a chave 'curso' existe e se o valor é 'História'
                if 'curso' in pessoa and pessoa['curso'] == 'História' and 'modalidade' in pessoa and pessoa['modalidade'] == 'Presencial':
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