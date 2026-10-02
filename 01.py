aluno = input("digite o nome do aluno")
ano_nascimento = int(input("digite o ano de nascimento do aluno"))
nota1 = float(input("digite a nota1 do aluno"))
nota2 = float(input("Digite a nota2 do aluno"))
media = (nota1 + nota2) / 2
ano_atual = 2026
idade = ano_atual - ano_nascimento

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print (f"Aluno: {aluno}")
print (f"Idade: {idade}")
print (f"Você está {situacao}")