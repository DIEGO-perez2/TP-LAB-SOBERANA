[infraestructura.md](https://github.com/user-attachments/files/28241457/infraestructura.md)# TP Laboratorio Unidad 4 - IA Soberana y Vibe Coding

## Integrante 1

Descripción:
Instalación y ejecución local de un modelo LLM utilizando herramientas open source dentro de una máquina virtual Linux. Se documenta el proceso de clonación del repositorio, configuración del entorno y pruebas iniciales.

## Integrante 2
[infraestructura.md](https://github.com/user-attachments/files/28279416/infraestructura.md)

Descripcion: Instalacion de Podman Desktop con WSL2. Creacion de la maquina virtual con 2CPUs, 2 GB de RAM y 10 GB de disco, ejecucion del contenedor de Ollama en el puerto 11434, descarga del modelo qwen2.5:0.5b de 397 MB, verificacion del funcionamiento con Ollama list y navegador, exposicion del servidor en http://localhost:11434/

## Comandos utilizados









```bash
# Crear máquina de Podman
podman machine init --cpus 2 --memory 2048 --disk-size 10

# Iniciar máquina
podman machine start

# Ejecutar Ollama
podman run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama docker.io/ollama/ollama

# Descargar modelo
podman exec ollama ollama pull qwen2.5:0.5b
## IP del servidor

- **IP:** `192.168.56.1`
- **Puerto:** `11434`
- **URL:** `http://localhost:11434/`

## Modelo usado
- **Nombre:** `qwen2.5:0.5b`
- **Tamaño:** 397 MB
- **Nombre:** `qwen2.5:0.5b`
- **Tamaño:** 397 MB
```
#Evidencia




Modelo descargado   


<img width="1317" height="878" alt="modelo-list" src="https://github.com/user-attachments/assets/ba1d2c12-7bc7-4c3a-9230-63fa64e17ba1" />





Ollama Corriendo ( " Ollama Running")



<img width="546" height="152" alt="ollama-running" src="https://github.com/user-attachments/assets/cfcdcd9d-80ca-4a5f-a6bb-d67703a902c7" />



# Scripting.md - Integrante 3

## Descripción

Se desarrolló un script en Python utilizando el paradigma de Vibe Coding.  
El código fue generado mediante asistencia de IA y probado contra el servidor local de Ollama desplegado por el Integrante 2.

## Modelo utilizado

- Modelo: qwen2.5:0.5b
- Endpoint: http://localhost:11434/api/generate

## Prompt inicial utilizado

```txt
Genera un script en Python que lea un archivo de texto y lo envíe a la API local de Ollama para obtener un resumen de 3 líneas.
```
Capturas de conversacion con IA( Chat GPT)

<img width="1280" height="636" alt="conversacion ia" src="https://github.com/user-attachments/assets/0a896fa2-c3d3-4fa5-89c3-131e0d77117c" />







<img width="1222" height="786" alt="scrip" src="https://github.com/user-attachments/assets/1916c13b-abff-4604-922f-e24bd356a295" />






