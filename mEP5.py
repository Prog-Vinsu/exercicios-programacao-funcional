def nomes(n, candidatos, i = 1):
    if i==(n+1):
        v = leValor(int)
        return votacao(v, n, candidatos, votos = [0]*(n+2))
    else:
        candidatos[i] = leValor(str)
        return nomes(n, candidatos, i+1)

def votacao(v, n, candidatos, votos, i = 0):
    if i == v:
        printResultado(n, candidatos, votos)
    else:
        vp = leValor(int)
        if vp == 0:
            votos[vp] += 1
            return votacao(v, n, candidatos, votos, i+1)
        elif vp != 0:
            if vp <= n:
                votos[vp] += 1
                return votacao(v, n, candidatos, votos, i+1)
            elif vp > n:
                votos[n+1] += 1
                votacao(v, n, candidatos, votos, i+1)

def printResultado(n, candidatos, votos, i = 1):
    if i == (n+1):
        print(f"Brancos: {votos[0]}")
        print(f"Nulos: {votos[n+1]}")
        soh_candidatos = votos[1:n+1]
        ganhador = verifica_maior_valor(soh_candidatos)
        print(f"Vencedor(a): {candidatos[ganhador+1]}")
    else:
        print(f"{candidatos[i]}: {votos[i]}")
        return printResultado(n, candidatos, votos, i + 1)

def verifica_maior_valor(lista, i = 0):
    if i <= len(lista):
        if lista[i] == max(lista):
            return i
        else:
            return verifica_maior_valor(lista, i+1)

def leValor(funcaoConv, msg = ""):
    try:
        return funcaoConv(input(msg))
    except:
        print("ERRO: Tipo inválido")
        return leValor(funcaoConv, msg)

def main():
    n = leValor(int)
    nomes(n, candidatos = [""]*(n+1))

main()