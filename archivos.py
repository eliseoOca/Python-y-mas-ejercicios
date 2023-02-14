# guardar datos en archivo
# abrimos el archivo

escritura= open("archivo.txt","w")
escritura.write(
    "Esto se escribe en el archivo\ny esto eb la linea siguiente \n\t\t\ty esto en otra linea tabulado")
escritura.close()

#lestura de fichero
lectura=open("archivo.txt","r")
#leemos una linea
leelinea=lectura.readline()
print("Leyendo una linea\n"+leelinea)
lectura.close()
#leemos todo el fichero
lectura=open("archivo.txt","r")
leetodo=lectura.read()#podemos usar readLines, que devuelve una lista con cada linea
#print(type(leetodo))
print("leemos todo \n"+leetodo)
lectura.close()