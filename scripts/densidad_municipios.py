municipios = [
    {"nombre": "Valladolid", "poblacion": 295639, "superficie": 197.91},
    {"nombre": "Burgos", "poblacion": 175821, "superficie": 107.08},
    {"nombre": "León", "poblacion": 124028, "superficie": 39.03}
]

for m in municipios:
    m["densidad"] = m["poblacion"] / m["superficie"]

municipios_ordenados = sorted(municipios, key=lambda x: x["densidad"], reverse=True)

print("Ranking por densidad:\n")

for m in municipios_ordenados:
    print(f"{m['nombre']} - {round(m['densidad'],2)} hab/km²")