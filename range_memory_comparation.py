# Crear dos rangos que parecen iguales
rango1 = range(5, 100, 2)
rango2 = range(5, 100, 2)
for i in rango1:
    print('i', i)

for j in rango2:
    print('j', j)

# Verificar si los rangos son iguales usando el operador "is"
son_iguales_con_is = rango1 is rango2
print("¿Los rangos son iguales usando 'is'?", son_iguales_con_is)

# Mostrar las direcciones de memoria de los rangos usando el operador "id"
direccion_memoria_rango1 = id(rango1)
direccion_memoria_rango2 = id(rango2)
print("Dirección de memoria de rango1:", direccion_memoria_rango1)
print("Dirección de memoria de rango2:", direccion_memoria_rango2)
