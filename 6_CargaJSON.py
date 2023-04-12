import json

# Abrir el archivo JSON y cargarlo en un objeto JSON
with open('EstadosUnidos.json', 'r') as f:
    lista_estados = json.load(f)

# Mostrar los estados
print(lista_estados)
