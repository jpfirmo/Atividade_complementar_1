salario = float(input("Digite seu salário: "))
valor_aumento = 15

aumento = valor_aumento / 100

valor_aumentado = salario * aumento

salario_final = salario + valor_aumentado

print(f"O salário final do funcionário com aumento é: R$ {salario_final:.2f}")