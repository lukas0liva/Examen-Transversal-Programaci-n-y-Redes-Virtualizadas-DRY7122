integrantes = [
    {"nombre": "Oscar", "apellido": "Camus"},
    {"nombre": "Miguel", "apellido": "Diaz"},
    {"nombre": "Lukas", "apellido": "Olivares"}
]
for integrante in integrantes:
    print(f"Nombre: {integrante['nombre']}, Apellido: {integrante['apellido']}")
numero_vlan = int(input("Ingrese el número de VLAN: "))
if 1 <= numero_vlan <= 1005:
    print("La VLAN corresponde al rango normal.")
elif 1006 <= numero_vlan <= 4094:
    print("La VLAN corresponde al rango extendido.")
else:
    print("El número ingresado no corresponde a un rango de VLAN válido.")
