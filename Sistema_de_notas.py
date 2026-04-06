"""🔹 Atividade 1: Sistema de notas

Crie um programa que:

Receba 3 notas
Calcule a média
Diga se o aluno foi:
Aprovado (≥7)
Recuperação (5–6.9)
Reprovado (<5)

👉 Extra: mostre também a maior e a menor nota """

"""Tem que cria um sistema para as notas não passarem de 10"""

nota1 = float(input("Digite sua Nota 1: "))
while nota1 > 10 or nota1 < 0:
    print("Nota inválida! Digite entre 0 e 10.")
    nota1 = float(input("Digite sua Nota 1: "))

nota2 = float(input("Digite sua Nota 2: "))
while nota2 > 10 or nota2 < 0:
    print("Nota inválida! Digite entre 0 e 10.")
    nota2 = float(input("Digite sua Nota 2: "))

nota3 = float(input("Digite sua Nota 3: "))
while nota3 > 10 or nota3 < 0:
    print("Nota inválida! Digite entre 0 e 10.")
    nota3 = float(input("Digite sua Nota 3: "))

nota_final = (nota1 + nota2 + nota3) / 3

print(f"Sua média foi: {nota_final:.1f}")

if nota_final >= 7:
    print("Aprovado")
elif 5 <= nota_final < 7:
    print("Recuperação")
else:
    print("Reprovado")

maior = max(nota1, nota2, nota3)
menor = min(nota1, nota2, nota3)

print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")