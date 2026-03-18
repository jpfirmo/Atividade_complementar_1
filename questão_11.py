produtos = {
    "arroz": 5.50,
    "feijao": 7.20,
    "macarrao": 4.00,
    "leite": 3.80
}

busca = input("Digite o nome do produto: ")

if busca in produtos:
    print("O preço do", busca, "é R$", produtos[busca])
else:
    print("Produto não encontrado")