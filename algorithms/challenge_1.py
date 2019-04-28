
 # -*- coding: utf-8 -*-

def suma(number):
    if number == 0:
	    return 0

    return number +suma(number - 1)

if __name__ == '__main__':
	number = int (input('Ingresa el numero que desea sumar recursivamente:'))

	result=suma(number)
	
	print('La suma de los {} primeros números es {}'.format(number, result))
