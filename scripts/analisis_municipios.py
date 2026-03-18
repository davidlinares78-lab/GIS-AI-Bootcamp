import csv

archivo = open("data/municipios.csv")

lector = csv.DictReader(archivo)

datos = []

for fila in lector:
    poblacion = int(fila["poblacion"])
    superficie = float(fila["superficie"])
    
    densidad = poblacion / superficie
    
    datos.append({
        "municipio": fila["municipio"],
        "densidad": densidad
    })
    
    datos_ordenados = sorted(datos, key=lambda x: x["densidad"], reverse=True)
    
    print("\nRanking densidad poblacional:\n")
    
    for d in datos_ordenados:
        print(f"{d['municipio']} -> {round(d['densidad'],2)} hab/km²")