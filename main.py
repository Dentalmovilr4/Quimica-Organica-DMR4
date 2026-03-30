import json
import os

def cargar_datos():
    try:
        with open('preguntas_quimica.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo preguntas_quimica.json")
        return None

def ejecutar_cuestionario():
    datos = cargar_datos()
    if not datos:
        return

    print(f"\n=== {datos['tema']} ===")
    print(f"Total de preguntas: {len(datos['preguntas'])}\n")

    for item in datos['preguntas']:
        print(f"Pregunta {item['id']}: {item['p']}")
        input("[Presiona Enter para ver la respuesta...]")
        print(f"Respuesta: {item['r']}\n" + "-"*30 + "\n")

if __name__ == "__main__":
    ejecutar_cuestionario()
