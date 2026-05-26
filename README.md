[infraestructura.md](https://github.com/user-attachments/files/28241457/infraestructura.md)# TP Laboratorio Unidad 4 - IA Soberana y Vibe Coding

## Integrante 1

Descripción:
Instalación y ejecución local de un modelo LLM utilizando herramientas open source dentro de una máquina virtual Linux. Se documenta el proceso de clonación del repositorio, configuración del entorno y pruebas iniciales.

#Integrante 2

## Comandos utilizados

#Crear máquina de Podman
podman machine init --cpus 2 --memory 2048 --disk-size 10

#Iniciar máquina
podman machine start

#Ejecutar Ollama
podman run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama docker.io/ollama/ollama

#Descargar modelo
podman exec ollama ollama pull qwen2.5:0.5b
## IP del servidor
- **IP:** `192.168.56.1`
- **Puerto:** `11434`
- **URL:** `http://192.168.56.1:11434`
## Modelo usado
- **Nombre:** `qwen2.5:0.5b`
- **Tamaño:** 397 MB

## evidencia
Ollama corriendo


.<img width="546" height="152" alt="ollama-running png" src="https://github.com/user-attachments/assets/40a2110b-621f-4a59-acf1-a0959f4a83c8" />




Modelo descargado



<img width="1317" height="878" alt="modelo-list png" src="https://github.com/user-attachments/assets/8c036ea5-f2cb-41cc-bece-0ca7aac9b3d5" />

