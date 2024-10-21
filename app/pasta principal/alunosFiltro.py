class AlunosFiltro:
    def filtroHistoria(self, dados):
        nomes_historia = []
        for pessoa in dados:
            if 'curso' in pessoa and pessoa['curso'] == 'História' and 'modalidade' in pessoa and pessoa['modalidade'] == "Presencial":
                if 'nome' in pessoa:
                    nomes_historia.append(pessoa['nome'])
                else:
                    print("Aviso: Encontrado aluno sem nome no JSON.")
        
        return nomes_historia  # Agora retorna a lista completa após o loop
