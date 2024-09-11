"""
kevin isaac torres jimenez
222h17061
examen diagnostico
"""
import cmath

def calcular_raices(a,b,c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1=(-b+cmath.sqrt(discriminante)/(2*a))
        x2=(-b-cmath.sqrt(discriminante)/(2*a))
    elif discriminante == 0:
        x1=x2=-b/(2*a)
    else:
        x1=(-b+cmath.sqrt(discriminante)/(2*a))
        x2=(-b-cmath.sqrt(discriminante)/(2*a))
    return x1, x2
def main():
    print("calcular las raices de los polinomios de segundo grado")
    try:
        a=float(input("introduce el valor de a (que no sea 0): "))
        if  a == 0:
            raise ValueError("el coeficiente que  introdujo es inccorrecto")
        b=float(input("introduce el valor de b: "))
        c=float(input("introduce el valor de c: "))

        x1,x2 = calcular_raices(a, b, c)

        print("las raices son:")
        print(f"x1={x1}")
        print(f"x2={x2}")
    except ValueError as e:
        print(f"ERROR{e}")
if __name__=="__main__":
    main()