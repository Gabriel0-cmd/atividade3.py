palavra = input("Digite uma palavra:")
vogais = 0

for letra in palavra:
  if letra.lower() in "aeiou":
    vogais = vogais + 1
    print("Total de vogais: ", vogais)