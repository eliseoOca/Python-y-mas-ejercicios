def dividir1():
    num1= int(input("dime el primer numero: "))
    num2= int(input("dime el primer numero: "))
    try:
        division = num1/num2
    except ZeroDivisionError:
        print("no se puede dividir por cero")
        division=0
    finally:
        return division
    

if __name__=="__main__":
    print(dividir1())