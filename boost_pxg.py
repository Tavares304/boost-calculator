#essa parte de variaveis são as tabelas de boost em forma de lista para serem acessadas

b2 = [0,1,2,4,6,9,12,16,20,25,30,36,42,49,56,64,72,81,90,100,110,121,132,144,156,169,182,196,210,225,240,256,272,289,306,324,342,361,380,400,420,441,462,484,506,529,552,576,600,625,650]
b3 = [0,1,2,3,5,7,9,12,15,18,22,26,30,35,40,45,51,57,63,70,77,84,92,100,108,117,126,135,145,155,165,176,187,198,210,222,234,247,260,273,287,301,315,330,345,360,376,392,408,425,442]
b4 = [0,1,2,3,4,6,8,10,12,15,18,21,24,28,32,36,40,45,50,55,60,66,72,78,84,91,98,105,112,120,128,136,144,153,162,171,180,190,200,210,220,231,242,253,264,276,88,300,312,325,338]
b5 = [0,1,2,3,4,5,7,9,11,13,15,18,21,24,27,30,34,38,42,46,50,55,60,65,70,75,81,87,93,99,105,112,119,126,133,140,148,156,164,172,180,189,198,207,216,225,235,245,255,265,275]
b6 = [0,1,2,3,4,5,6,8,10,12,14,16,18,21,24,27,30,33,36,40,44,48,52,56,60,65,70,75,80,85,90,96,102,108,114,120,126,133,140,147,154,161,168,176,184,192,200,208,216,225,234]
b7 = [0,1,2,3,4,5,6,7,9,11,13,15,17,19,21,24,27,30,33,36,39,42,46,50,54,58,62,66,70,75,80,85,90,95,100,105,111,117,123,129,135,141,147,154,161,168,175,182,189,196,204]
b8 = [0,1,2,3,4,5,6,7,8,10,12,14,16,18,20,22,24,27,30,33,36,39,42,45,48,52,56,60,64,68,72,76,80,85,90,95,100,10,110,115,120,126,132,138,144,150,156,162,168,175,182]
b9 = [0,1,2,3,4,5,6,7,8,9,11,13,15,17,19,21,23,25,27,30,33,36,39,42,45,48,51,54,58,62,66,70,74,78,82,86,90,95,100,105,110,115,120,125,130,135,141,147,153,159,165]
b10 = [0,1,2,3,4,5,6,7,8,9,10,12,14,6,18,20,22,24,26,28,30,33,36,39,42,45,48,51,54,57,60,64,68,72,76,80,84,88,92,96,100,105,110,115,120,125,130,135,140,145,150]
b15 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,94,98,105,106,110]
b20 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,63,66,69,72,75,78,81,84,87,90]
b25 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75]
b30 = [0,0,1,0,2,0,3,0,4,0,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65]



#essa parte sao para asinformações que o player passa

nome_do_pokemon = str(input("Qual o nome do pokemon?: "))
boost_atual = int(input("Qual o boost atual do pokemon?: "))
boost_pretendido = int(input("Até que level quer boostar o pokemon?: "))
boost = int(input("Qual o boost desse pokemon? (taxa de boost): "))
custo_stone = int(input("Qual o valor que sera pago por cada stone usada? EX: 5000: "))



#  calculos prontos hehe :)


if (boost==2):
    calculo = b2[boost_pretendido] - b2[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==3):
    calculo = b3[boost_pretendido] - b3[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==4):
    calculo = b4[boost_pretendido] - b4[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==5):
    calculo = b5[boost_pretendido] - b5[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==6):
    calculo = b6[boost_pretendido] - b6[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==7):
    calculo = b7[boost_pretendido] - b7[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==8):
    calculo = b8[boost_pretendido] - b8[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==9):
    calculo = b9[boost_pretendido] - b9[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==10):
    calculo = b10[boost_pretendido] - b10[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==15):
    calculo = b15[boost_pretendido] - b15[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==20):
    calculo = b20[boost_pretendido] - b20[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==25):
    calculo = b25[boost_pretendido] - b25[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
elif (boost==30):
    calculo = b30[boost_pretendido] - b30[boost_atual]
    print("Sera necessario ", calculo, "stones para boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
    valor_gasto = calculo*custo_stone
    print("Sera gasto ", float(valor_gasto), "em stones boostar o ",nome_do_pokemon, "do boost +",boost_atual, "até o boost +", boost_pretendido )
