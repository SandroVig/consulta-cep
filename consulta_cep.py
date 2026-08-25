# consulta_cep.py
import requests
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados
def exibir_endereco(dados):
    print("CEP:", dados["cep"])
    print("Rua:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:", dados["localidade"])
    print("Estado:", dados["uf"])
while True:
    print("\n=== Consulta de CEP ===")
    print("1 - Buscar um CEP")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cep = input("Digite o CEP (só números): ")
        dados = consultar_cep(cep)
        exibir_endereco(dados)
    elif opcao == "2":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")