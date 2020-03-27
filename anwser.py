distancia = int(input("distancia a recorrer: "))
tipo = int(input("nacional(1) internacional(2)"))
pesoT=0

while (pesoT<337250):
    peso = int(input("Peso de equipaje: "))
    pesoT=pesoT+peso
    if (peso<10):
        print("El peso no es aceptable")
    else:
        if (pesoT>355000):
            print("el peso ha superado la capacidad maxima, este peso no es aceptado")
            pesoT=pesoT-peso
        else:
            if (tipo==1):
                valorT=peso*4500 + distancia*4000
            elif (tipo==2):
                valorT=peso*4500 + (distancia*0.621371)*8000
            else:
                print("tipo de vuelo no valido")
            if (peso>100 and tipo==1):
                valorT=valorT*0.85
            elif(distancia>8000 and tipo==2 and peso>400):
                valorT=valorT*0.9

print("Valor Total: ",valorT)



