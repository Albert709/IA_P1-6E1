entrada = input('Ingresa un color escrito con minúsculas:\n')
colores = ('negro', 'rosa', 'verde', 'azul')

if entrada in colores[0]:
    print('El color negro está admitido')
elif entrada in colores[1]:
    print('El color rosa está admitido')
if entrada in colores[2]:
    print('El color verde está admitido')
elif entrada in colores[3]:
    print('El color azul está admitido')
else:
    print('Color no admitido')

