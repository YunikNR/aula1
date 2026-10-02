# Crie um algoritmo que leia 3 valores (lados de um triângulo)
# Determine se formam um triângulo
# se é equilátero, isósceles ou escaleno.

# Lendo os 3 valores (lados do triângulo)
ladoA = float(input("Qual o lado A?"))
ladoB = float(input("Qual o lado B?"))
ladoC = float(input("Qual o lado C?"))

# Verificando se forma um triângulo
if (ladoA + ladoB) > ladoC and (ladoA + ladoC) > ladoB and (ladoB + ladoC) > ladoA:  
    condicao = "Forma um triângulo"
else:
    condicao = "Não forma um triângulo"

# Reconhecer se é equilátero, isósceles ou escaleno

if condicao == "Forma um triângulo":
    if ladoA == ladoB and ladoC == ladoB:
        tipo = "também é equilátero"
    if ladoA != ladoB and ladoA != ladoC:
        tipo = "também é isósceles"
    if ladoA != ladoB and ladoA != ladoC:
        tipo = "também é escaleno"
else:
    tipo = "consequentemente não tem forma"

# Falar todas as informações

print(f"{condicao} e {tipo}")