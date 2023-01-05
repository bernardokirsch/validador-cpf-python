cpf = str(input('Informe seu CPF: '))
validacao_1 = 0
validacao_final = 0
valido_1 = True
valido_2 = True

if len(cpf) != 11 or cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '88888888888' or cpf == '99999999999' or cpf == '01234567890' :
    print('CPF inválido')
else: 
    for i in range(9):
        if i == 0:
            validacao_1 = (int(cpf[i]) * 10) + validacao_1
        elif i == 1:
            validacao_1 = (int(cpf[i]) * 9) + validacao_1
        elif i == 2:
            validacao_1 = (int(cpf[i]) * 8) + validacao_1
        elif i == 3:
            validacao_1 = (int(cpf[i]) * 7) + validacao_1
        elif i == 4:
            validacao_1 = (int(cpf[i]) * 6) + validacao_1
        elif i == 5:
            validacao_1 = (int(cpf[i]) * 5) + validacao_1
        elif i == 6:
            validacao_1 = (int(cpf[i]) * 4) + validacao_1
        elif i == 7:
            validacao_1 = (int(cpf[i]) * 3) + validacao_1
        elif i == 8:
            validacao_1 = (int(cpf[i]) * 2) + validacao_1

    validacao_1_div = int(validacao_1 / 11)

    validacao_1_resto = validacao_1 - (11 * validacao_1_div)

    if validacao_1_resto == 0 or validacao_1_resto == 1:
        if int(cpf[9]) == 0:
            valido_1 = True
        else:
            valido_1 = False


    elif validacao_1_resto >= 2 and validacao_1_resto <= 10:
        validacao_1_dig = 11 - validacao_1_resto
        if validacao_1_dig == int(cpf[9]):
            valido_1 = True
        else:
            valido_1 = False

    for i in range(10):
        if i == 0:
            validacao_final = (int(cpf[i]) * 11) + validacao_final
        elif i == 1:
            validacao_final = (int(cpf[i]) * 10) + validacao_final
        elif i == 2:
            validacao_final = (int(cpf[i]) * 9) + validacao_final
        elif i == 3:
            validacao_final = (int(cpf[i]) * 8) + validacao_final
        elif i == 4:
            validacao_final = (int(cpf[i]) * 7) + validacao_final
        elif i == 5:
            validacao_final = (int(cpf[i]) * 6) + validacao_final
        elif i == 6:
            validacao_final = (int(cpf[i]) * 5) + validacao_final
        elif i == 7:
            validacao_final = (int(cpf[i]) * 4) + validacao_final
        elif i == 8:
            validacao_final = (int(cpf[i]) * 3) + validacao_final
        elif i == 9:
            validacao_final = (int(cpf[i]) * 2) + validacao_final

    validacao_final_div = int(validacao_final / 11)

    validacao_final_resto = validacao_final - (11 * validacao_final_div)

    if validacao_final_resto == 0 or validacao_final_resto == 1:
        if int(cpf[10]) == 0:
            valido_2 = True
        else:
            valido_2 = False

    elif validacao_final_resto >= 2 and validacao_final_resto <= 10:
        validacao_final_dig = 11 - validacao_final_resto
        if validacao_final_dig == int(cpf[10]):
            valido_2 = True
        else:
            valido_2 = False
            
    if valido_1 == True and valido_2 == True:
        print('CPF válido')
    else: 
        print('CPF inválido')

    if int(cpf[8]) == 0:
        print('O CPF foi cadastrado no Rio Grande do Sul - RS')
    elif int(cpf[8]) == 1:
        print('O CPF foi cadastrado em alguma dessas localidades: Distrito Federal - DF, Goiás - GO, Mato Grosso - MT, Mato Grosso do Sul - MS ou Tocantins - TO')
    elif int(cpf[8]) == 2:
        print('O CPF foi cadastrado em alguma dessas localidades: Amazonas - AM, Pará - PA, Roraima - RR, Amapá - AP, Acre - AC ou Rondônia - RO')
    elif int(cpf[8]) == 3:
        print('O CPF foi cadastrado em alguma dessas localidades: Ceará - CE, Maranhão - MA ou Piauí - PI')
    elif int(cpf[8]) == 4:
        print('O CPF foi cadastrado em alguma dessas localidades: Paraíba - PB, Pernambuco - PE, Alagoas - AL ou Rio Grande do Norte - RN')
    elif int(cpf[8]) == 5:
        print('O CPF foi cadastrado em alguma dessas localidades: Bahia - BA ou Sergipe - SE')
    elif int(cpf[8]) == 6:
        print('O CPF foi cadastrado em Minas Gerais - MG')
    elif int(cpf[8]) == 7:
        print('O CPF foi cadastrado em alguma dessas localidades: Rio de Janeiro - RJ ou Espírito Santo - ES')
    elif int(cpf[8]) == 8:
        print('O CPF foi cadastrado em São Paulo - SP')
    elif int(cpf[8]) == 9:
        print('O CPF foi cadastrado em alguma dessas localidades: Paraná - PR ou Santa Catarina - SC')