import math
import sys

"""
Programa el cual esta diseñado para obtener la integral por el metodo numerico de la regla de Simpson 
Utilizando High order functions y un sistema de precisión estilo derivada.

Se debe programar la funcion en python y luego se le debera pasar esta a la funcion precisionChecker 
en formato 
a = inicio del rango de integracion
b = final del rango de integracion
h = el numero de segmentos sobre el cual se iterara <-- este debe ser un numero par
mathFunction = Esta es la high order function que usara la funcion de Simpson para poder calcular la integral 
                de forma dinamica.
"""

E = .0000001
PI = math.pi#el numero PI
a = 0
b = 0
h = 0

#Checked
def recieveABH():
    """
    Funcion que recibe los inputs especificos para esta funcion y hace una pequeña validacion
    """
    inputs = sys.argv
    if(len(inputs)<4):
        print("Some parameters are still needed, please send them like A B H")
        return False
    else:
        global a,b,h
        try:
            a = abs(float(inputs[1]))
            b = abs(float(inputs[2]))
            h = abs(int(inputs[3]))
            if(h%2 != 0):
                print(f"the number h ({h}), must be an integer even number")
                return False
        except ValueError:
            print("A value given to the program cannot be converted to a floating point number")
            return False
    return True#EOFunction

#Checked
def simpson(a,b,h,mathFunction):
    """
    Funcion que hace la integral de mathFunction(x) desde a hasta b en pasos de h
    usando la formula de integracion de la regla de simpson.
    """
    W = b/h
    I = mathFunction(a) + mathFunction(b)#el inicio y el final de la funcion
    for i in range(1,h):
        value = 2*mathFunction(i*W)
        if(i%2 == 1):#es impar i
            value *= 2
        I += value
    return I * (W/3)#EOFunction

#Checked
def precisionChecker(a,b,h,mathFunction):
    """
    Function to make sure the results you are getting are as precise a you need them to be.
    If the evaluation with the double of points that you inputed is better, then it shall be the final result.
    """
    F0 = simpson(a,b,h,mathFunction)
    h *= 2
    F1 = simpson(a,b,h,mathFunction)
    while( abs(F1-F0) > E):
        print(F0)
        F0 = F1
        h *= 2
        F1 = simpson(a,b,h,mathFunction)
    print(f"Final result = {F1}")
    return F1#EOFunction

valid = recieveABH()
if(valid):
    #You must change the None in the next line with a math function written in python in order for the 
    #simpson numeric method to work.
    finalResult = precisionChecker(a,b,h,None) #<-- You must change this line for it to work properly