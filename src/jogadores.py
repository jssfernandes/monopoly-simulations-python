import random


jogadores = {0: {'nome': 'Impulsivo'}, 1: {'nome': 'Exigente'},
            2: {'nome': 'Cauteloso'}, 3: {'nome': 'Aleatório'}}

nomes = ['Impulsivo', 'Exigente', 'Cauteloso', 'Aleatório']
random.shuffle(nomes)

for jogador in jogadores:
    jogadores[jogador].update(
        caixa=300, posicao_atual=-1, propriedades=[], jogadas=0, start='', nome=nomes[jogador])

jogadores[0]['start'] = True

def jogadores_reset():
    jogadores = {0: {'nome': 'Impulsivo'}, 1: {'nome': 'Exigente'},
            2: {'nome': 'Cauteloso'}, 3: {'nome': 'Aleatório'}}

    nomes = ['Impulsivo', 'Exigente', 'Cauteloso', 'Aleatório']
    random.shuffle(nomes)

    for jogador in jogadores:
        jogadores[jogador].update(
            caixa=300, posicao_atual=-1, propriedades=[], jogadas=0, start='', nome=nomes[jogador])

    jogadores[0]['start'] = True

    return jogadores

def excluir_jogador(jogadores, jogador_atual, tabuleiro, resumoA):
    if jogadores[jogador_atual]['caixa'] < 0:
        print('O jogador', jogadores[jogador_atual]['nome'], 'perdeu e sera removido!!!')

        for id, info in tabuleiro.items():
            if info['proprietario'] == jogadores[jogador_atual]['nome']:
                info['proprietario'] = ''

        resumoA[jogador_atual].update(jogadores.pop(jogador_atual))
