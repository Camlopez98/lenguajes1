""""
import importlib.util
import json
clientes = {
    "cedula":1233691138,
    "nombre": "Camilo",
    "apellido": "lopez",
    "edad": 30,
    "email": "camilo.lopez@example.com",
}
ruta = "clientes.py"


 #escritura de un archivo json
with open(cliente.json_path,"w") as clientes_json:
    #serializar  - dict -> json

    
    json.dump(clientes_json_dict, clientes_json, indent=2)
"""
import json

def guardar_en_json():
    clientes = {
        "cedula": 1233691138,
        "nombre": "Camilo",
        "apellido": "lopez",
        "edad": 30,
        "email": "camilo.lopez@example.com"
    }

    with open("clientes.json", "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

# Llamar a la función
guardar_en_json()