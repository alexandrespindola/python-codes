tempo_viagem = int(input())
velocidade_media = int(input())
VELOCIDADE_AUTOMOVEL = 12
distancia = tempo_viagem * velocidade_media
gasto_combustivel = distancia / VELOCIDADE_AUTOMOVEL
print('{:.3f}'.format(gasto_combustivel))