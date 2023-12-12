maior_pontuacao = 0
result_f = open("results.txt")
for line in result_f:
    (name,resultado) = line.split()
    if float(resultado) > maior_pontuacao:
        maior_pontuacao = float(resultado)
result_f.close()
print("A maior pontuacao é a: ")
print(resultado[0])
print(resultado[2])
print(resultado[3])
