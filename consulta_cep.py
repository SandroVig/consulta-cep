# consulta_cep.py
import requests
cep = "01310930"
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()
print(dados)