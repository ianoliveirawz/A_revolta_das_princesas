print ("A revolta das princesas")
print (" olá jogador(a), seja bem vindo!")
print (" esse jogo representa o combate das princesas")
print ("que usaram seus poderes para combater")
print (" os jogadores teram 100 hp")
print ("os nomes dos personagens são Branca de leite e a Pé solto")
print (" quem atacará primeiro será a Branca de leite")
print("a Branca de leite irá usar a arma que atira maçãs, e o feitiço do sono da morte")
print(" a branca de leite tirou 10 de hp")
print("o segundo personagem que ira atacar será a Pé solto")
print(" a Pé solto ira atacar tenis, e tera o feitiço de transformar o seu adversario em abobora")
print("a pé solto tirou 20 hp")
print("nome1=Branca de leite, nome2=Pé solto")

print("nome do jogador 1= Branca de leite")
print("nome do jogador 2= Pé solto ")
hp1=100
hp2=100
dano1=10
dano2=20
soma1=100-10
soma2=100-20
print("quem ganhou foi a pé solto")

hp1 = 100
hp2 = 100 

while hp1 > 0 and hp2 > 0:
    print("branca de leite atacou!")
    hp2 = hp2 -10
    print(" HP da pe solto:", hp2)

    if hp2 <= 0:
        print("branca de leite venceu")
        break
        
    print("pe solto atacou!")
    hp1 =hp1 - 20
    print("hp da branca de leite:", hp1)

    if hp1 <= 0:
        print("pe solto venceu")
        break

print ("A revolta das princesas")

hp1 =100
hp2 =100

for rodada in range(1,4):

    print("\n--- rodada", rodada, "---")

    print("escolha o ataque da branca de leite")
    print("1 - magia")
    print("2 - chute")

    escolha = int(input("digite o número do ataque: "))

    if escolha == 1 :
        dano = 20
        print ("branca de leite usou magia")
    else:
        dano = 10
        print (" branca de leite usou chute")

    hp2 = hp2 - dano

    print("HP da pé solto:", hp2)

    print("\nfim da batalha")

    if hp2 <= 0:
        print(" branca de leite venceu")
        print(" fim da batalha")
        break

    else:
        print(" pé solto venceu")

    print (" A revolta das princesas")
    hp2 = 100

    for rodada in range(1,6):

        print("\n--- rodada", rodada, "---")

        print("escolha o ataque:")
        print("1 - magia")
        print("2 - chute")
        print("3 - espada")
        print("4 - fogo")

        escolha = int(input(" digite o numero do ataque: "))

        if escolha == 1:
            dano=20
            print("branca de leite usou magia")

        elif escolha == 2:
            dano = 20
            print(" branca de leite usou chute")

        elif escolha == 3:
            dano = 30
            print(" branca de leite usou espada")

        elif escolha == 4:
            dano = 40
            print("branca de leite usou fogo")

        else:
            dano = 0
            print(" ataque invalido")

            hp2 = hp2 - dano

            print("HP da pe solto:",hp2)

            if hp2 <= 0:
                break

            print("\nfim da batalha")

            if hp2 <= 0:
                print(" branca de leite venceu")

            elif hp1 <= 0:
                print("pe solto venceu")
            


  

    

 





