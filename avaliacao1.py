n, t = map(int, input().split())

jogadores = []

for i in range(n):
    nome, habilidade = input().split()
    habilidade = int(habilidade)

    jogadores.append((nome, habilidade))

jogadores.sort(key=lambda x: x[1], reverse=True)


times = []

for i in range(t):
    times.append([])

time_atual = 0

for jogador in jogadores:

    times[time_atual].append(jogador)

    time_atual += 1

    if time_atual == t:
        time_atual = 0

for time in times:
    time.sort()

for i in range(t):
    print(f"Time {i + 1}")

    for jogador in times[i]:
        print(jogador[0])

    print()
