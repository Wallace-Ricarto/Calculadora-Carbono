# Solicita ao usuário o tipo de combustível
operação = input("Qual o tipo de combustível? 1-Gasolina 2-Diesel 3-Etanol 4-Eletricidade ")

if operação == "1":
    # Informações sobre o uso de gasolina
    dia = int(input("Você utiliza seu veículo por quantos dias na semana? "))
    km = int(input("Qual é a média de KM que você percorre por dia? "))
    litro = int(input("Quantos KM por litro o seu carro faz? "))

    # Cálculo das emissões de CO2 da gasolina
    soma2 = (dia * 52) * km
    taxaLitroporKm = soma2 / litro
    emissaoGasolina = taxaLitroporKm * 0.740 * 2.28
    toneladaGasolina = emissaoGasolina * 0.001
    arvoresGasolina = (emissaoGasolina / 130) * 0.994
    arvorenmrarredondado = round(arvoresGasolina)
    reais = toneladaGasolina * 26
    dolares = toneladaGasolina * 5

    # Exibe as emissões de carbono e as opções de compensação para gasolina
    print(f'A emissão de carbono nesse trajeto de {dia} dias durante um ano é: {emissaoGasolina:.2f} KG de CO₂')
    print(f'O total de toneladas obtido foi de {toneladaGasolina:.2f} Toneladas')

    compensacaoGasolina = input("Como deseja compensar a emissão de carbono? 1- Crédito de carbono  2- Plantio de Árvores")
    
    if compensacaoGasolina == "1":
        print(f'Seu veículo emitiu cerca de {toneladaGasolina:.2f} Toneladas de CO₂')
        print(f'O valor atual de cada tonelada que deixa de ser emitida é de US$ 5 ou R$ 26 no Brasil')
        print(f'Portanto, você deve pagar {reais:.2f} R$ ou {dolares:.2f} US$')
    
    if compensacaoGasolina == "2":
        print(f'Você precisa plantar {arvorenmrarredondado} árvores por ano na Mata Atlântica ')

elif operação == "2":
    # Informações sobre o uso de diesel
    dia = int(input("Você utiliza seu veículo por quantos dias na semana? "))
    km = int(input("Qual é a média de KM que você percorre por dia? "))
    litro = int(input("Quantos KM por litro o seu carro faz? "))

    # Cálculo das emissões de CO2 do diesel
    soma2 = (dia * 52) * km
    taxaLitroporKm = soma2 / litro
    emissaoDiesel = taxaLitroporKm * 0.853 * 3.2
    toneladaDiesel = emissaoDiesel * 0.001
    arvoresDiesel = (emissaoDiesel / 130) * 0.994
    arvoredieselaredondado = round(arvoresDiesel)
    reaisDiesel = toneladaDiesel * 26
    dolaresDiesel = toneladaDiesel * 5

    # Exibe as emissões de carbono e as opções de compensação para diesel
    print(f'A emissão de carbono nesse trajeto de {dia} dias utilizando Diesel foi de: {emissaoDiesel:.2f} KG de CO₂-eq')
    print(f'O total de toneladas obtido foi de {toneladaDiesel:.2f} Toneladas')

    compensacaoDiesel = input("Como deseja compensar a emissão de carbono? 1- Crédito de carbono  2- Plantio de Árvores")
    
    if compensacaoDiesel == "1":
        print(f'Seu veículo emitiu cerca de {toneladaDiesel:.2f} Toneladas de CO₂')
        print(f'O valor atual de cada tonelada que deixa de ser emitida é de US$ 5 ou R$ 26 no Brasil')
        print(f'Portanto, você deve pagar {reaisDiesel:.2f} R$ ou {dolaresDiesel:.2f} US$')
    
    if compensacaoDiesel == "2":
        print(f'Você precisa plantar {arvoredieselaredondado} árvores por ano na Mata Atlântica ')

elif operação == "3":
    # Informações sobre o uso de etanol
    dia = int(input("Você utiliza seu veículo por quantos dias na semana? "))
    km = int(input("Qual é a média de KM que você percorre por dia? "))
    litro = int(input("Quantos KM por litro o seu carro faz? "))

    # Cálculo das emissões de CO2 do etanol
    soma2 = (dia * 52) * km
    taxaLitroporKm = soma2 / litro
    emissaoEtanol = taxaLitroporKm * 0.789 * 2.03
    toneladaEtanol = emissaoEtanol * 0.001
    arvoresEtanol = (emissaoEtanol / 130) * 0.994
    arvoresEtanolaredondado = round(arvoresEtanol)
    reaisEtanol = toneladaEtanol * 26
    dolaresEtanol = toneladaEtanol * 5

    # Exibe as emissões de carbono e as opções de compensação para etanol
    print(f'A emissão de carbono nesse trajeto de {dia} dias utilizando Etanol foi de: {emissaoEtanol:.2f} KG de CO₂')
    print(f'O total de toneladas obtido foi de {toneladaEtanol:.2f} Toneladas')

    compensacaoEtanol = input("Como deseja compensar a emissão de carbono? 1- Crédito de carbono  2- Plantio de Árvores")
    
    if compensacaoEtanol == "1":
        print(f'Seu veículo emitiu cerca de {toneladaEtanol:.2f} Toneladas de CO₂')
        print(f'O valor atual de cada tonelada que deixa de ser emitida é de US$ 5 ou R$ 26 no Brasil')
        print(f'Portanto, você deve pagar {reaisEtanol:.2f} R$ ou {dolaresEtanol:.2f} US$')
    
    if compensacaoEtanol == "2":
        print(f'Você precisa plantar {arvoresEtanolaredondado} árvores por ano na Mata Atlântica ')
        
elif operação == "4":
    dia = int(input("Você utiliza seu veículo por quantos dias na semana? "))
    km = int(input("Qual é a média de KM que você percorre por dia? "))
    kwh = int(input("Quantos kWh o seu veiculo consome por KM? "))
    #Emissões de CO2 (g/km) = (Consumo de eletricidade (kWh/km) * Emissões de CO2 da eletricidade (g/kWh))
    #Conforme o Ministério da Ciência e Tecnologia, o fator de emissão de CO2 produzido na geração de energia elétrica pela matriz energética é de 0,0817 KG/KWh, determinado na Tabela 1
    eficiencia= (kwh/km) * 0.0817
    soma2 = (dia * 52) * km
    emissaoEletrico = eficiencia / soma2
    print(f'A emissão de carbono nesse trajeto de {dia} dias utilizando veiculo eletrico foi de: {emissaoEletrico:.2f} KG de CO₂')
    print(f'O total de toneladas obtido foi de {emissaoEletrico:.2f} Toneladas')
    if soma2 > 385:
        recargaBateria= soma2/385
        recargaBateria=round(recargaBateria)
        emissaoEnergia=recargaBateria * 21.1
        toneladaEnergia=emissaoEnergia * 0.001
        reaisEletrico= toneladaEnergia * 26
        dolaresEletrico= toneladaEnergia * 5
        arvoresEletrico=(emissaoEnergia / 130) * 0.994
        arvoresEletricoaredondado=round(arvoresEletrico)
        print(f'Durante um ano você recarregou o seu veiculo cerca de {recargaBateria} vezes')
        print(f'A emissão de carbono nesse trajeto de {dia} dias utilizando Eletricidade foi de: {emissaoEnergia:.2f} KG de CO₂')
        print(f'O total de toneladas obtido foi de {toneladaEnergia:.2f} Toneladas')
        
        compensacaoEnergia = input("Como deseja compensar a emissão de carbono? 1- Crédito de carbono  2- Plantio de Árvores")
        if compensacaoEnergia == "1":
         print(f'Seu veículo emitiu cerca de {toneladaEnergia:.2f} Toneladas de CO₂')
         print(f'O valor atual de cada tonelada que deixa de ser emitida é de US$ 5 ou R$ 26 no Brasil')
         print(f'Portanto, você deve pagar {reaisEletrico:.2f} R$ ou {dolaresEletrico:.2f} US$')
    
    if compensacaoEnergia == "2":
        print(f'Você precisa plantar {arvoresEletricoaredondado} árvores por ano na Mata Atlântica ')
    else:
        print("Operação invalida! ")