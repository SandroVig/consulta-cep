# consulta_cep.py
import json
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
    print("3 - Salvar histórico em arquivo")
    print("4 - Sair")
    
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
        else:
            for item in historico: 
                rua = item.get("logradouro") or "Sem logradouro"
                print(item.get("cep", "N/A"), "-", rua) 
                
    elif opcao == "3": 
        with open("historico.json", "w", encoding="utf-8") as arquivo:
            json.dump(historico, arquivo, indent=2, ensure_ascii=False)
        print("Histórico salvo em historico.json!") 
        
    elif opcao == "4":
        print("Até logo!")
        break
        
    else:
        print("Opção inválida.")