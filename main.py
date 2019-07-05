import random

def check_level(sel_level):
    levels = ['0','1','2']
    if not(sel_level in levels):
        sel_level = input('Elige un valor correcto para el nivel (0,1 o 2)')
        check_level(sel_level)
    else:        
        if sel_level == '0':
            print('Escoge un número del 1 al 100. Tienes 10 intentos')
            niveles(0)
        elif sel_level == '1':
            print('Escoge un número del 1 al 100. Tienes 6 intentos')
            niveles(1)
        else:
            print('Escoge un número del 1 al 100. Tienes 3 intentos')
            niveles(2)

def help_guess(guess,count,correct_guess,limit):
    if guess == correct_guess:
        if count == 0:
            print('Eres un master')
        elif (count < 5):
            print('¡Felicidades! Adivinaste mi número!')
        else:
            print('¡Lo has logrado pero adivinar no es lo tuyo, mejor invita las chelas!')
        return count + 1,1
    elif (guess > correct_guess and count < limit-1):
        print('El número es menor. Escoge uno más chico')
        return count + 1,0
    elif (guess < correct_guess and count < limit-1):
        print('El número es mayor. Escoge uno más grande')
        return count + 1,0
    else:
        return count + 1,0
    
def niveles(n_nivel):
    count = 0
    acaba = 0
    random0 = random.randrange(1,100)
    if n_nivel == 0:
        limit_tries = 10
    elif n_nivel == 1:
        limit_tries = 6
    else:
        limit_tries = 3
    while count < limit_tries and acaba == 0:
        num_escogido = int(input('Escoge un número: '))
        count,acaba = help_guess(num_escogido, count, random0,limit_tries)
        if (acaba == 0 and count < limit_tries):
            print('Este fue tu intento número:', count,' Te quedan ',limit_tries - count)
        elif (acaba == 0 and count == limit_tries):
            print('Ese fue tu último intento')
    if acaba == 0:
        print('Perdiste, no sabes adivinar. \n¡Debes las chelas!')

name = input('¿Cuál es tu nombre?')
bienvenida = '\nEn este juego deberás adivinar el número en el que estoy pensando del 1 al 100. \n¡Ten cuidado! De no adivinar en el número de intentos permitido, pagarás las chelas :) \nTienes 10 intentos para nivel principiante, 6 para nivel intermedio y 3 para nivel avanzado. \n¡Suerte!'
print(f'¡Bienvenido {name}!', bienvenida)
level = input('Escoge uno de los siguientes niveles: Principiante = 0, Intermedio = 1, Avanzado = 2')
check_level(level)