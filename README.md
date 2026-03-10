**Scientific PDF Analysis Pipeline**


**1. Descripción**

Este proyecto implementa un pipeline reproducible para el análisis de artículos científicos en formato PDF.
El sistema utiliza GROBID para extraer información de documentos académicos y posteriormente 
analiza los resultados para obtener estadísticas y gráficas.

**2. Estructura del repositorio**

src/trabajo1/       # Código principal del pipeline
tests/              # Tests realizados
input/              # Entrada de datos en forma de PDFs
output/             # Salida de datos/resultados en forma de graficas y estadísticas
docker-compose.yml  # Ejecución con Docker
Dockerfile          # Imágen del programa
pyproject.toml      # Dependencias de python
poetry.lock
CITATION.cff
README.md

**3. Requisitos**

 - Para ejecutar el proyecto se necesita:

Python 3.10+
Docker
Poetry

 - Dependencias principales del proyecto:

requests
matplotlib
wordcloud
GROBID

**4. Instalación y ejecución**

Existen dos formas posibles de ejecutar el proyecto:

  **1.** Entorno python (POETRY)
  Este método permite ejecutar el pipeline utilizando un entrono python local, pero requiere que el servicio
  GROBID este levantado en un contenedor Docker.

  PASOS:
    - Instalar dependencias : > poetry install
    - Levantar contenedor GROBID por defecto : > docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0
    - Introducir los datos que se desean procesar en input/
    - Ejecutar el pipeline : > poetry run python src/trabajo1/main.py

  **2.** Ejecución con compose (DOCKER)
  Este metodo, mas recomendable, permite ejecutar el programa de forma mas sencilla utilizando Docker Compose,
  que levanta automáticamente todos los servicios necesarios.
    
  PASOS:
    - Introducir los datos que se desean procesar en input/
    - Construir y ejecutar los servicios : > docker compose up --build

**5. Resultados**

El pipeline genera en output/ varios archivos de salida:

  - links.txt                 — lista de enlaces detectados
  - figures_per_article.png   — gráfico con número de figuras por artículo
  - wordcloud.png             — nube de palabras generada a partir del texto


**6. Limitaciones**

El sistema presenta algunas limitaciones:

  1. Requiere que el servicio GROBID esté disponible para procesar los PDFs.
  2. Funciona mejor con artículos científicos estructurados, ocumentos PDF escaneados o
  con formato no estándar pueden producir resultados incompletos.
  4. A la ejecución de los scripts se le fuerza una espera minima de 20 segundos para dar tiempo a GROBID.
  5. El procesamiento de documentos grandes puede tardar varios segundos por archivo.

