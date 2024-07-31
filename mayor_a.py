import sys

def meses_mayores_a_umbral(umbral, datos):   # Diccionario para almacenar los resultados
    resultado = {}
    
    # Itera sobre los elementos del diccionario original
    for mes, valor in datos.items():      # Si el valor supera el umbral, añadir al diccionario de resultados
        if valor > umbral:
            resultado[mes] = valor
    
    
    return resultado  # Devolver el diccionario filtrado

try:
    umbral = int(sys.argv[1])
except (IndexError, ValueError):
    print("Debe proporcionar un umbral válido como argumento.")
    sys.exit(1)

# Diccionario con los datos de ejemplo
datos = {
    'Enero': 25000,
    'Febrero': 15000,
    'Marzo': 30000,
    'Abril': 35000,
    'Mayo': 81000,
    'Junio': 20000,
    'Julio': 19000,
    'Agosto': 41200,
    'Septiembre': 10000,
    'Octubre': 29000,
    'Noviembre': 91000,
    'Diciembre': 23000
} 
# Obtiene los meses que superan el umbral
resultado = meses_mayores_a_umbral(umbral, datos)
print(resultado)