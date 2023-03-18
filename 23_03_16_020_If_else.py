#color = rojo

#else color == rojo
#Print "El color es rojo."
#if color != rojo
#Print "El color no es rojo."

#Para corregirlo, debemos primero comenzar con if, para después aplicar el else, algunos problemas de sintaxis y ya quedará 
#de la siguiente manera
color = "rojo"

if color == "rojo":
    print('El color es rojo.')
else:
    print('El color no es rojo.')