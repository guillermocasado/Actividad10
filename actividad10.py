from stats_data import StatsData

lista = []

num =""

while(num.lower() != "fin"):
    num = input("Dime un numero: ")
    if(num.lower() != "fin"):
        lista.append(float(num))


sd = StatsData(lista)

print('Lista de números: ', sd.l_data)
print('Media: ', sd.media)
print('Mediana: ', sd.mediana)
print('Varianza: ', sd.varianza)

