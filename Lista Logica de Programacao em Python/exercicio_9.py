import math

r = float(input("Informe o valor do raio da lata em cm: "))
h = float(input("Informe a altura da lata em cm: "))

volume = math.pi * (r ** 2) * h

print (f"O volume da lata é: {volume/1000: .2f} litros")

