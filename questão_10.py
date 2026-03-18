def analisar_lista(lista):
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    return maior, menor, soma

numeros = []

for i in range(5):
    num = float(input("Digite um número: "))
    numeros.append(num)

maior, menor, soma = analisar_lista(numeros)

print("Maior número:", maior)
print("Menor número:", menor)
print("Soma total:", soma)