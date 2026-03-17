preco = float(input("Digite o preço do produto: "))
valor_desconto = int(input("Digite o percentual de desconto: "))

desconto = valor_desconto / 100

valor_produto = preco * desconto

preco_final = preco - valor_produto

print(f"O preço final do produto com desconto é: R$ {preco_final:.2f}")