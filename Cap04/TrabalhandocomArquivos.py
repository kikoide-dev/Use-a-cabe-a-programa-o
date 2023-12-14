highest_score = 0

with open("results.txt") as result_f:
    for line in result_f:
        parts = line.strip().split()  # Divide a linha em partes usando espaços em branco como delimitadores
        if len(parts) == 2:  # Certifica-se de que existem duas partes na linha (nome e pontuação)
            current_score = float(parts[1])  # A segunda parte deve ser a pontuação
            if current_score > highest_score:
                highest_score = current_score

print("A maior nota é:")
print(highest_score)