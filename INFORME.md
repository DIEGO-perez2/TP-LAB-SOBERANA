# INFORME - LABORATORIO IA SOBERANA

## Integrantes

| Integrante      | Rol             |
| --------------- | --------------- |
| Diego Pérez     | Maintainer      |
| Selena Cayumil  | Infraestructura |
| Rocío Farinelli | Scripting       |

## Introducción

El presente trabajo tuvo como objetivo implementar un laboratorio colaborativo utilizando herramientas de software libre y un modelo de inteligencia artificial ejecutado localmente. Para ello se emplearon entornos virtualizados, control de versiones mediante Git y trabajo colaborativo a través de GitHub.

## Herramientas utilizadas

* VirtualBox
* Ubuntu Linux
* Git
* GitHub
* Podman Desktop
* Ollama
* Modelo Qwen 2.5:0.5b

## Distribución de Roles

### Maintainer - Diego Pérez

Responsable de la administración del repositorio, integración de cambios mediante Pull Requests, organización de ramas y consolidación de la documentación final.

### Infraestructura - Selena Cayumil

Responsable de la instalación y configuración del entorno Linux, herramientas de virtualización y ejecución local del modelo.

### Scripting - Rocío Farinelli

Responsable del desarrollo de scripts y automatizaciones requeridas por la consigna.

## Flujo Git Implementado

Cada integrante trabajó sobre una rama independiente para evitar conflictos y permitir un desarrollo paralelo.

* principal
* maintainer-setup
* infraestructura
* scripting

Los cambios fueron integrados mediante Pull Requests revisados por el maintainer.

## Desarrollo

### Configuración del entorno virtual

Se creó una máquina virtual utilizando VirtualBox con Ubuntu Linux como sistema operativo base.

### Configuración de Git

Se configuró Git con credenciales individuales y se vinculó el repositorio remoto alojado en GitHub.

### Implementación de Ollama

Se instaló Ollama y se descargó el modelo Qwen 2.5:0.5b para realizar pruebas locales de inferencia.

## Problemas Encontrados

Durante el desarrollo surgieron inconvenientes relacionados con permisos, sincronización de ramas y configuración del entorno virtual.

## Soluciones Aplicadas

Los problemas fueron resueltos mediante actualización de dependencias, corrección de permisos y utilización de Pull Requests para integrar cambios de manera controlada.

## Reflexión sobre Soberanía Tecnológica

La ejecución local de modelos abiertos permite mayor control sobre los datos y reduce la dependencia de servicios externos. Esta experiencia permitió comprender la importancia de utilizar herramientas abiertas para promover independencia tecnológica y transparencia.

## Conclusión

El trabajo permitió integrar virtualización, control de versiones y herramientas de inteligencia artificial dentro de un entorno colaborativo. La utilización de ramas, Pull Requests y roles diferenciados facilitó la organización del proyecto y la trazabilidad de las contribuciones de cada integrante.
