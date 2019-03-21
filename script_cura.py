

# Abrir fichero para lectura y escritura. El puntero se posiciona al principio del fichero
fichero = open('datos', 'r+')


# Abrir fichero de salida para lectura y escritura. El puntero se posiciona al principio del fichero
ficherosalida = open('datossalida', 'rw+')


# Cargamos todas las lineas en una lista y calculamos numlineas
lineas = fichero.readlines()
numlineas = len(lineas)
numlayer = 1


# Bucle for que calcula el nº de layer en el fichero
for i in range(numlineas):
  linea = str(lineas[i])
  if ( linea[0:4] == "LAYER" )
    numlayer += 1

porcentaje = numlineas/100
layer = 1
p = 0
nl = 0

# Escritura del archivo final

for i in numlineas:
  linea = str(lineas[i])
  nl += 1
  if ( linea[0:4] == "LAYER)
    ficherosalida.write("M117 L=", layer,"/",numlayer," P=",p ,"%/n")
    layer += 1
  ficherosalida.write(linea)
  if ( nl >= porcentaje )
    ficherosalida.write("M117 L=", layer,"/",numlayer," P=",p ,"%/n")
    nl = 1
    p += 1
  
ficherosalida.close()
fichero.close()
