## jogo de jokenpo com python

import random
from random import choice

print("Bem vindo(a) ao jogo Jokenpô")
nome_jogador = input("Digite o seu nome: ")

contador_jogador = 0
contador_maquina = 0

while True:
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha = input("O que você vai jogar? \n"
                    "    🪨 Pedra \n"
                    "    📄 Papel \n"
                    "    ✄ Tesoura \n"
                    "    Qual sua escolha: ").strip().lower()
    if escolha not in opcoes:
        print("Essa não é uma opção valida, tente novamente inserindo uma das opções informadas")
        continue
    else:
        escolha_maquina = choice(opcoes)
        print(f'A maquina escolhe: {escolha_maquina}')
        if escolha == escolha_maquina:
            escolha_empate = input("🏁 Vocês empataram! \n"
                                   "deseja tentar novamente? (sim/não) ").strip().lower()
            if escolha_empate == "sim":
                continue
            else:
                print("Foi um bom jogo! Até logo!")
                break

        if escolha != escolha_maquina:
            if (escolha == "pedra" and escolha_maquina == "tesoura") or \
                    (escolha == "papel" and escolha_maquina == "pedra") or \
                    (escolha == "tesoura" and escolha_maquina == "papel"):
                print("🏆🎉 Parabéns!! Você venceu")
                contador_jogador += 1

            else:
                print("💔🥀 A maquina ganhou! sinto muito")
                contador_maquina += 1

            print("O placar atual esta:")
            print(f'Maquina: {contador_maquina} X {nome_jogador}: {contador_jogador}')

            continuar_jogo2 = input("Você deseja continuar a jogar? (sim/não) ").strip().lower()
            if continuar_jogo2 == "sim":
                continue
            else:
                print("Foi um bom jogo! Até logo")
                break
