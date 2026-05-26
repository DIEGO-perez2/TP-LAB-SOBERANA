import requests

# Leer archivo de texto
with open("prueba.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# Prompt para la IA
prompt = f"Resume el siguiente texto en 3 líneas:\n\n{contenido}"

# Datos para Ollama
datos = {
    "model": "qwen2.5:0.5b",
    "prompt": prompt,
    "stream": False
}

# Enviar petición
respuesta = requests.post(
    "http://localhost:11434/api/generate",
    json=datos
)

# Mostrar respuesta
resultado = respuesta.json()

print("\nResumen generado:\n")
print(resultado["response"])
