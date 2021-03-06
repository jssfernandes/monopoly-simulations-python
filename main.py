from collections import OrderedDict
from datetime import datetime
from operator import getitem
from random import randint
from src.comportamento import impulsivo, exigente, cauteloso, aleatorio
from src.estado import resumoA, rodadas, total_jogadas, rodadasA, estado_reset, vencedoresA, tempodeA, tempoSec
from src.finalizando import finalizando
from src.jogadores import jogadores_reset, excluir_jogador
from src.pagar_aluguel import pagar_aluguel
from src.tabuleiro import tabuleiro, tabuleiro_reset


simulacoes = 0

while simulacoes < 300:
    simulacoes += 1
    print('Simulação = ', simulacoes)
    if simulacoes == 20000:
        jogadores = jogadores_reset()
        tabuleiro = tabuleiro_reset()
        resumoA = estado_reset()
        startgame(rodadas, total_jogadas, jogadores)
    try:
        print('try,...')
        def startgame(rodadas, total_jogadas, jogadores):
            inicio_partida = datetime.now()
            while rodadas < 1000 and len(jogadores) != 1:

                rodadas += 1
                for jogador_atual in list(jogadores):

                    jogadores[jogador_atual]['jogadas'] += 1
                    dado = randint(1, 6)

                    if jogadores[jogador_atual]['jogadas'] != 0:
                        jogadores[jogador_atual]['caixa'] = jogadores[jogador_atual]['caixa'] + 100

                    print('----' * 42)
                    print('{} jogou o dado e o valor é {}'.format(jogadores[jogador_atual]['nome'], dado))
                    print('----' * 42)

                    if jogadores[jogador_atual]['posicao_atual'] <= len(tabuleiro):
                        jogadores[jogador_atual]['posicao_atual'] = jogadores[jogador_atual]['posicao_atual'] + dado

                    if jogadores[jogador_atual]['posicao_atual'] >= len(tabuleiro):
                        jogadores[jogador_atual]['posicao_atual'] = abs(
                            (len(tabuleiro)) - (jogadores[jogador_atual]['posicao_atual'] + dado - 1))

                    print('O jogado {} esta na propriedade {} {}'.format(jogadores[jogador_atual]['nome'],
                                                                         jogadores[jogador_atual]['posicao_atual'],
                                                                         tabuleiro[jogadores[jogador_atual][
                                                                             'posicao_atual']]))
                    print('Regras especiais aplicadas a esse jogador...')

                    pagar_aluguel(tabuleiro, jogadores, jogador_atual)

                    if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] == '':
                        print('----' * 42)
                        print('Propriedade disponível para compra')
                        print('----' * 42)

                        if jogadores[jogador_atual]['nome'] == 'Impulsivo':
                            impulsivo(tabuleiro, jogadores, jogador_atual)

                        if jogadores[jogador_atual]['nome'] == 'Exigente':
                            exigente(tabuleiro, jogadores, jogador_atual)

                        if jogadores[jogador_atual]['nome'] == 'Cauteloso':
                            cauteloso(tabuleiro, jogadores, jogador_atual)

                        if jogadores[jogador_atual]['nome'] == 'Aleatório':
                            aleatorio(tabuleiro, jogadores, jogador_atual)

                    excluir_jogador(jogadores, jogador_atual, tabuleiro, resumoA)

                    print('PROXIMO JOGADOR ..')
                    total_jogadas += 1
            tempo_decorrido = datetime.now() - inicio_partida
            if len(jogadores) == 1:
                if 0 in jogadores:
                    jogador_atual = 0
                    vencedoresA.append(jogadores[jogador_atual]['nome'])
                    print('====' * 42)
                    print('O JOGADOR', jogadores[jogador_atual]['nome'], 'é o VENCEDOR', vencedoresA)
                    finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec,
                                vencedoresA, )
                elif 1 in jogadores:
                    jogador_atual = 1
                    vencedoresA.append(jogadores[jogador_atual]['nome'])
                    print('====' * 42)
                    print('O JOGADOR', jogadores[jogador_atual]['nome'], 'é o VENCEDOR', vencedoresA)
                    finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec,
                                vencedoresA, )
                elif 2 in jogadores:
                    jogador_atual = 2
                    vencedoresA.append(jogadores[jogador_atual]['nome'])
                    print('====' * 42)
                    print('O JOGADOR', jogadores[jogador_atual]['nome'], 'é o VENCEDOR', vencedoresA)
                    finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec,
                                vencedoresA, )
                elif 3 in jogadores:
                    jogador_atual = 3
                    vencedoresA.append(jogadores[jogador_atual]['nome'])
                    print('----' * 42)
                    print('O JOGADOR', jogadores[jogador_atual]['nome'], 'é o VENCEDOR', vencedoresA)
                    finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec,
                                vencedoresA, )
                else:
                    print('====' * 42)
                    print('====' * 42)
                    print('Mil Partidas ta bom né... temos vencedores...', vencedoresA)
                    finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec,
                                vencedoresA, )
                    print('----' * 42)
            if len(jogadores) >= 2:
                desempate = OrderedDict(sorted(jogadores.items(), key=lambda x: getitem(x[1], 'caixa'), reverse=True))
                vencedoresA.append(next(iter(desempate.values()))['nome'])
                print('----' * 42)
                print('O JOGADOR', next(iter(desempate.values()))['nome'], 'é o VENCEDOR', vencedoresA)
                finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec,
                            vencedoresA, )

        jogadores = jogadores_reset()
        tabuleiro = tabuleiro_reset()
        resumoA = estado_reset()
        startgame(rodadas, total_jogadas, jogadores)

    except ValueError:
        print('falha não prevista...')
