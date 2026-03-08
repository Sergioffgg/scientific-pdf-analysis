from pathlib import Path
from grobid_client import process_pdf
from analysis import extract_abstract, count_figures, extract_links
from plots import plot_wordcloud, plot_figures
import time

print("Esperando a GROBID...")
time.sleep(20)


pdf_dir = Path("input")
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

abstracts = []
figure_counts = {}
all_links = {}

pdfs = list(pdf_dir.glob("*.pdf"))
if not pdfs:
    print("No se han encontrado archivos PDF en: /input")
    exit()

num = 0
for pdf in pdfs:
    num += 1
    if num > 10:
        print("\n ### Máximo de archivos (10) alcanzado, el resto de archivos serán omitidos ### \n")
        break

    print(f"    | [{num}] Procesando {pdf.name}")
    xml = process_pdf(pdf)

    abstract = extract_abstract(xml)
    abstracts.append(abstract)

    figure_counts[pdf.name] = count_figures(xml)
    all_links[pdf.name] = extract_links(xml)

# Añadir a nube de palabras #

plot_wordcloud(" ".join(abstracts))

# Añadir a grafica de figuras#

plot_figures(figure_counts)

# Escribir archivo de links #

with open("output/links.txt", "w") as f:
    for paper, links in all_links.items():
        f.write(f"{paper}:\n")
        for link in links:
            f.write(f"  {link}\n")

print("=====================================================================")
print("¡Analisis realizado con exito!")
print("Resultados guardados en: /output")
print("=====================================================================")