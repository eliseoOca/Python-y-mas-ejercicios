def guardarTXT(nombreArchivo, txt):
    try:
        fichero=open(nombreArchivo+'.txt','w')
        fichero.write(txt)
        print('texto guardado')
    except Exception:
        print('ha ocurrido un error')
    finally:
        fichero.close()
    return True

def leeTXT(nombreArchivo):
    try:
        fichero=open(nombreArchivo+'.txt','r')
        txt=fichero.read()
        return txt
    except Exception:
        print('ha ocurrido un error')
    finally:
        fichero.close()
        
txt=input('ingresa el texto a guardar guardar: ')
archivo=input('indica en nombre del archivo')
guardarTXT(archivo,txt)
txt=leeTXT(archivo)
print('este es el texto guardado')
print(txt)
