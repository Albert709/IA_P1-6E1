def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')#4 argumentos
colores('lila', 'negro', 'rojo')#3 argumentos
colores('rosa')#1 argumento
colores('marrón', 'naranja')#2 argumentos

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'negro')

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de la suma es de:', resultado)


suma(54, 123, 35, 432, 12)
