######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP3 - Ironman
# Nome: Vincenzo Tognere Polonini
# Matrícula: 2022100364
######################################################
def main():
    sexo = input()
    idade = int(input())
    t_natacao = int(input())
    t1 = int(input())
    t_ciclismo = int(input())
    t2 = int(input())
    t_corrida = int(input())
    tempo_total = t_natacao + t1 + t_ciclismo + t2 + t_corrida
    horas, minutos = conversor_tempo(tempo_total)
    limite_h, limite_m = verifica_idade(sexo, idade)
    tempo_em_seg, tempo_total_seg = limite_hora_p_seg(limite_h, limite_m, tempo_total)
    diferenca = tempo_em_seg - tempo_total_seg
    dif_h = diferenca // 3600
    dif_min = (diferenca % 3600) // 60
    if sexo == "m" or sexo == "M":
        print(f"Tempo do atleta: {horas:02d}h {minutos:02d}min")
        print(f"Tempo necessario: {limite_h:02d}h {limite_m:02d}min")
        if diferenca >= 0:
            print("Conseguiu indice? SIM")
            print(f"O atleta terminou a prova {(dif_h):02d}h {(dif_min):02d}min abaixo do indice")
        else:
            diferenca = tempo_total_seg - tempo_em_seg
            dif_h = diferenca // 3600
            dif_min = (diferenca % 3600) // 60
            print("Conseguiu indice? NAO")
            print(f"O atleta terminou a prova {(dif_h):02d}h {(dif_min):02d}min acima do indice")
    else:
        print(f"Tempo da atleta: {horas:02d}h {minutos:02d}min")
        print(f"Tempo necessario: {limite_h:02d}h {limite_m:02d}min")
        diferenca = tempo_total_seg - tempo_em_seg
        if diferenca <= 0:
            print("Conseguiu indice? SIM")
            print(f"A atleta terminou a prova {(dif_h):02d}h {(dif_min):02d}min abaixo do indice")
        else:
            diferenca = tempo_total_seg - tempo_em_seg
            dif_h = diferenca // 3600
            dif_min = (diferenca % 3600) // 60
            print("Conseguiu indice? NAO")
            print(f"A atleta terminou a prova {(dif_h):02d}h {(dif_min):02d}min acima do indice")
    
def limite_hora_p_seg(limite_h, limite_m, tempo_total):
    return (limite_h * 3600) + (limite_m * 60), tempo_total * 60

def conversor_tempo(tempo_total):
    '''Funcao que converte o tempo total em minutos para horas e minutos.'''
    horas = tempo_total // 60
    minutos = tempo_total % 60
    return horas, minutos

def verifica_idade(sexo, idade):
    if sexo == "m" or sexo == "M":
        if idade >= 18 and idade <= 29:
            return 8, 0
        elif idade <= 34:
            return 8, 10
        elif idade <= 39:
            return 8, 25
        elif idade <= 44:
            return 8, 35
        elif idade <= 49:
            return 8, 50
        elif idade <= 54:
            return 9, 0
        elif idade <= 59:
            return 9, 15
        elif idade <= 64:
            return 9, 30
        elif idade <= 69:
            return 9, 50
        elif idade <= 74:
            return 10, 20
        elif idade <= 79:
            return 11, 0
        elif idade>=80:
            return 12, 0
    if sexo == "f" or sexo == "F":
        if idade >= 18 and idade <= 29:
            return 8, 10
        elif idade <= 34:
            return 8, 20
        elif idade <= 39:
            return 8, 40
        elif idade <= 44:
            return 9, 0
        elif idade <= 49:
            return 9, 20
        elif idade <= 54:
            return 9, 40
        elif idade <= 59:
            return 10, 0
        elif idade <= 64:
            return 10, 30
        elif idade <= 69:
            return 11, 0
        elif idade <= 74:
            return 11, 45
        elif idade <= 79:
            return 12, 30
        elif idade >=80 :
            return 13, 30
        
main()