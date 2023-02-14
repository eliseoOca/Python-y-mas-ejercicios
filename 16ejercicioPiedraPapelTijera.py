import random
import sys

def iniciar():
    global partidas, ganadas, perdidas, empatadas
    partidas=0
    ganadas=0
    perdidas=0
    empatadas=0
    
def menu():
    print("""
          Indica el numero de la opcion seleccionada:
          1. piedra
          2. papel
          3. tijera
          0. salir
          """)
    opcion= input("->")
    if opcion not in ['1','2','3','0']:
        print('selecciona una opcion valida\n')
        opcion_usuario=None
    else:
        if opcion=='1':
            opcion_usuario='piedra'
        if opcion=='2':
            opcion_usuario='papel'
        if opcion=='3':
            opcion_usuario='tijera'
        if opcion=='0':
            print('hasta pronto!!!')
            sys.exit()
    return opcion_usuario

def comprobar(opcion_usuario, opcion_maquina):
    global partidas,ganadas,perdidas,empatadas
    partidas+=1
    print("\n")
    if (opcion_usuario==opcion_maquina):
        print("empate")
        empatadas+=1
    elif(opcion_usuario=="piedra") and (opcion_maquina=="tijera"):
        print("gane")
        ganadas+=1
    elif(opcion_usuario=="papel") and (opcion_maquina=="piedra"):
        print("perdi")
        perdidas+=1
    elif(opcion_usuario=="tijera")and (opcion_maquina=="papel"):
        print("gane")
        ganadas+=1
    else:
        print("perdi")
        perdidas+=1
    print("\n")
    print("*"*20)
    print(f"mi opcion fue {opcion_maquina}")
    print(f"tu opcion fue{opcion_usuario}")
    print(f"llevamos {perdidas} perdidas")
    print(f"llevamos {ganadas} ganadas")
    print(f"llevamos {perdidas} partidas")
    print(f"llevamos {empatadas} empatadas")
    print("*"*20)
    print("\n")
def main():
    iniciar()
    opcion_usuario=menu()
    while True:
        if opcion_usuario !=None:
            opcion_maquina=elige_maquina()
            comprobar(opcion_usuario,opcion_maquina)
        opcion_usuario=menu()
if __name__=='__main__':
    main()
        