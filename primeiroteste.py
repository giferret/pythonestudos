print("Programa para cálculo de CR CEDERJ UFF\n")

soma = 0.0
chTotal = 0

regCH = 1
print("Carga horária %d (informe 0 para encerrar): " % regCH, end="")
ch = int(input())

while ch != 0:
    print("Nota final %d: " % regCH, end="")
    nota = float(input())

    soma += ch * nota
    chTotal += ch

    regCH += 1
    print("\nCarga horaria %d (informe 0 para encerrar): " % regCH, end="")
    ch = int(input())

if chTotal != 0:
    cr = soma / chTotal
else:
    cr = 0

print("\nSeu CR é %1.2f." % cr)