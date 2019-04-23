#Métodos para maipular strings
print("#Métodos para maipular strings")
var_string = "var_string = Initial text"
print (var_string)
print('-'*75)

new_string = var_string.upper()
print ("var_string.upper = ", new_string, " | Convert text to capital letters" )
print('-'*75)

new_string = var_string.lower()
print ("var_string.lower = ", new_string, " | Convert text to lowercase letters" )
print('-'*75)

new_string = var_string.find("a")
print ("var_string.find('a') = ", new_string, "  | Show the first character´s position in the text string, is case sensitive " )

new_string = var_string.find("i")
print ("var_string.find('i') = ", new_string, "  | Remember is case sensitive " )

new_string = var_string.find("z")
print ("var_string.find('z') = ", new_string, " | If there´s not a character the result is -1 " )

print('-'*75)

new_string = var_string.capitalize()
print ("var_string.capitalize = ", new_string, "| Convert the first character of the string into a capital letter")

print('-'*75)

if var_string.startswith('i'):
	print("if var_string.endswith('i'): print ('it´s true, te strings starts with: 'i' ')")
	print('it´s true, te strings ends with: "i"')

print('-'*75)

if var_string.endswith('t'):
	print("if var_string.endswith('t'): print ('it´s true, te strings ends with: 't' ')")
	print('it´s true, te strings ends with: "t"')

print('-'*75)
print('-'*75)

#Operadores de pertenencia, nos permiten sabes si un substring, es decir una subsecuencia se encuentra en la secuencia mayor 
#Por ejemplo la subsecuencia col esta dentro de colombia
#Distingue entre maysuculas y minusculas
print ("Operadores de pertenencia")
var_string = "Hola"
print ('var_string = "Hola"')
if "Ho" in var_string :
	print('if "Ho" in var_string :')
	print('The substring "Ho" is into the string "Hola" ')

print('-'*75)

if "mundo!" not in var_string :
	print('if "mundo!" not in var_string :')
	print('var_string += "mundo!"')
	var_string += " mundo!"
	print("var_string = ", var_string)	

#La función global dir nos dice los métodos que podemos utilizar dentro de un objeto
print('-'*75)
print('The dir() function, show us all the methods that we can use with an element')
print('For example:')
print('dii(car_string)')
print ( dir(var_string) )
print('-'*75)

print('-'*75)

def my_function():
	"""Este es un texto de ayuda de como utilizar esta funcion"""
	pass

print(help(my_function))

print('-'*75)
print("Presiona enter para salir")
input()