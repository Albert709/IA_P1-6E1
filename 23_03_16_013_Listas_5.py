colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores)
#del colores y almacena
guardar1 = colores.pop(1)
guardar2 = colores.pop(-2)
#asignar a nueva lista
nueva_lista = [guardar1, guardar2]
print(colores)
print(nueva_lista)
