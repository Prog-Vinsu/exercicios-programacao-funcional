peso = float(input())
idade = int(input())
if idade >= 16 and idade < 18:
    doc = input()
saude = input()
drogas = input()
doacao = input()
if doacao == "N":
    meses_ultima_doacao = int(input())
    doacoes_12_meses = int(input())
sexo = input()
if sexo == "F":
    gravidez = input()
    amamentacao = input()
    if amamentacao == "S":
        idade_bebe_amam = int(input())

print(f"Peso: {peso}")
print(F"Idade: {idade}")
if idade >= 16 and idade < 18:
    print(f"Documento de autorizacao: {doc}")
print(f"Boa saude: {saude}")
print(f"Uso drogas injetaveis: {drogas}")
print(f"Primeira doacao: {doacao}")
if doacao == "N":
    print(f"Meses desde ultima doacao: {meses_ultima_doacao}")
    print(f"Doacoes nos ultimos 12 meses: {doacoes_12_meses}")
print(f"Sexo biologico: {sexo}")
if sexo == "F":
    print(f"Gravidez: {gravidez}")
    print(f"Amamentando: {amamentacao}")
    if amamentacao == "S":
        print(f"Meses bebe: {idade_bebe_amam}")

aux = True
if peso < 50:
    print("Impedimento: abaixo do peso minimo.")
    aux = False
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    aux = False
elif 16 <= idade < 18 and doc == "N":
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    aux = False
elif idade >= 60  and idade <= 69 and doacao == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    aux = False
elif idade > 69:
    print("Impedimento: maior de 69 anos.")
    aux = False
if saude == "N":
    print("Impedimento: nao esta em boa saude.")
    aux = False
if drogas == "S":
    print("Impedimento: uso de drogas injetaveis.")
    aux = False
if doacao == "N":
    if sexo == "M":
        if meses_ultima_doacao <= 2:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            aux = False
        if doacoes_12_meses >= 4:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            aux = False
    if sexo == "F":
        if meses_ultima_doacao <= 3:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            aux = False
        if doacoes_12_meses >= 3:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            aux = False
if sexo == "F":
    if gravidez == "S":
        print("Impedimento: gravidez.")
        aux = False
    if amamentacao == "S" and idade_bebe_amam <= 12:
        print("Impedimento: amamentacao.")
        aux = False
if aux:
    print("Procure um hemocentro.")