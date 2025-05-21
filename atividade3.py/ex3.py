numeros = []

n1 = int(input("Digite um número inteiro:"))
n2 = int(input("Digite um número inteiro:"))
n3 = int(input("Digite um número inteiro:"))

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)

dobrados = []
dobrados.append(n1 * 2)
dobrados.append(n2 * 2)
dobrados.append(n3 * 2)

print("Números originais:", numeros)
print("Números multiplicados por 2:", dobrados)

soma_original = n1 + n2 + n3
soma_dobrados = dobrados[0] + dobrados[1] + dobrados[2]

print("Soma dos números originais:", soma_original)
print("Soma dos números multiplicados por 2:", soma_dobrados)