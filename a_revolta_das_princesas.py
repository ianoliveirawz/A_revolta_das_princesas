print (" a revolta das princesas")
print ("olá jogador, seja bem vindo")
print ("este jogo representa o combate das princesas que usam seus foguetes")
print ("nossas lutadoras são: branca de leite e pe solto.\n")

#configuraçoes da batalha real
hp_branca=100
hp_pe_solto=100
rodada = 0

# O loop continua enquanto as duas estiverem vivas
while hp_branca > 0 and hp_pe_solto > 0:
    rodada += 1
    print(f"\n---RODADA{rodada}---")
    print(f"HP branca de leite : {hp_branca} | HP pe solto : {hp_pe_solto}")

    # ===TURNO DA BRANCA DE LEITE===
    print("\n[turno da branca de leite] escolha o ataque:")
    print("1 - chute (10 de dano)")
    print("2 - magia (20 de dano)")
    print("3 - espada (30 de dano)")

    escolha = int(input("digite o numero de ataque: "))

    if escolha==1:
        dano = 10
        print("branca de leite usou chute")
    elif escolha ==2:
        dano = 20
        print("branca de leite usou magia")
    elif escolha==3:
        dano = 30
    else:
        dano == 0
        print (" ataque invalido! voce perdeu a vez")

    hp_pe_solto -= dano
    print(f"HP da pe solto agora é: {hp_pe_solto}")

    #verifique se a pe solto foi derrotada
    if hp_pe_solto <= 0:
        print("\n[turno da pe solto] ela contra ataca com tenis e abobora")
        dano_inimigo = 20
        hp_branca -= dano_inimigo
        print(f"pe solto causou {dano_inimigo} de dano")
        print(f"HP da branca de leite agora é: {hp_branca}")

        #verifique se a branca de leite foi derrotada

        if hp_branca <= 0:
            print("\n branca de leite foi derrotada")
            print("=== PE SOLTO VENCEU O JOGO!===")
            break
            
            #MUITO IMPORTANTE: avança para proxima rodada antes de repetir a loop
       
        print("\n === FIM DA BATALHA ===")
            



          
