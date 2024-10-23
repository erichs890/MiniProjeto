import requests

class LivroModelo:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    def getLivro(self):
        response = requests.get(self.urlBase)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar dados")
            return []
