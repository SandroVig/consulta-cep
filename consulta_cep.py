# consulta_cep.py
import requests

historico = [] 

def limpar_cep(cep): 
    return cep.replace("-", "").replace(".", "").strip() 

def cep_valido(cep): 
    return cep.isdigit() and len(cep) == 8 

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def exibir_endereco(dados):
    print("CEP:", dados.get("cep", "N/A"))
    print("Rua:", dados.get("logradouro", "N/A"))
    print("Bairro:", dados.get("bairro", "N/A"))
    print("Cidade:", dados.get("localidade", "N/A"))
    print("Estado:", dados.get("uf", "N/A"))

while True:
    print("\n=== Consulta de CEP ===")
    print("1 - Buscar um CEP") 
    print("2 - Ver histórico de buscas") 
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        cep_input = input("Digite o CEP: ")
        cep = limpar_cep(cep_input)
        
        if not cep_valido(cep):
            print("CEP inválido! Digite exatamente 8 números.")
            continue
            
        dados = consultar_cep(cep)
        
        
        if dados.get("erro"):
            print("CEP não encontrado.")
            continue
            
        exibir_endereco(dados)
        historico.append(dados)
        
    elif opcao == "2": 
        if not historico: 
            print("Nenhuma busca feita ainda.") 
        for item in historico: 
            print(item["cep"], "-", item["logradouro"]) 
    elif opcao == "3": 
        print("Até logo!") 
        break 
        
    else:
        print("Opção inválida.")