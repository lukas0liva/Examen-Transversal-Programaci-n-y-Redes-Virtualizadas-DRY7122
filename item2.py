import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radio de la Tierra en kilómetros
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia_km = R * c
    distancia_millas = distancia_km * 0.621371
    
    return distancia_km, distancia_millas

def calcular_tiempo(distancia_km, medio):
    velocidades = {
        "auto": 100,
        "autobús": 80,
        "tren": 120,
        "avión": 800
    }
    if medio in velocidades:
        return distancia_km / velocidades[medio]
    else:
        return None

ciudades = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Córdoba": (-31.4201, -64.1888),
    "Rosario": (-32.9442, -60.6505),
    "Mendoza": (-32.8908, -68.8272),
    "La Plata": (-34.9205, -57.9536),
    "Mar del Plata": (-38.0055, -57.5426),
    "San Miguel de Tucumán": (-26.8083, -65.2176),
    "Santiago": (-33.4489, -70.6693),
    "Valparaíso": (-33.0458, -71.6197),
    "Concepción": (-36.8201, -73.0444),
    "Puerto Montt": (-41.4718, -72.9362),
    "Antofagasta": (-23.6509, -70.3975),
    "Iquique": (-20.2208, -70.1431)
}

print("Ciudades disponibles:")
for ciudad in ciudades.keys():
    print(ciudad)

while True:
    print("\nIngrese 's' para salir en cualquier momento.")
    origen = input("Ciudad de Origen: ").strip()
    if origen.lower() == 's':
        break

    destino = input("Ciudad de Destino: ").strip()
    if destino.lower() == 's':
        break

    if origen not in ciudades or destino not in ciudades:
        print("Una o ambas ciudades no están en la lista. Por favor, intente de nuevo.")
        continue

    lat1, lon1 = ciudades[origen]
    lat2, lon2 = ciudades[destino]
    
    distancia_km, distancia_millas = haversine(lat1, lon1, lat2, lon2)
    
    print("Medios de transporte disponibles: auto, autobús, tren, avión")
    medio = input("Seleccione el medio de transporte: ").strip()
    if medio.lower() == 's':
        break

    tiempo = calcular_tiempo(distancia_km, medio)
    if tiempo is None:
        print("Medio de transporte no válido. Por favor, intente de nuevo.")
        continue
    
    print(f"\n--- Narrativa del viaje ---")
    print(f"De {origen} a {destino}:")
    print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
    print(f"Medio de transporte: {medio}")
    print(f"Duración estimada del viaje: {tiempo:.2f} horas\n")
