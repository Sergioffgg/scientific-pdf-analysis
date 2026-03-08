import matplotlib.pyplot as plt
from wordcloud import WordCloud


#### Nube de palabras ####

def plot_wordcloud(text):
    
    if not text.strip():
        print("No se pudo generar nube de palabras, texto inaccesible")
        return
    
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig("output/wordcloud.png")
    plt.close()


#### Grafico de figuras ####

def plot_figures(counts):

    if not counts.values() or not counts.keys():
        print("No se pudo generar grafico de conteo de figuras, datos inaccesibles")
        return

    plt.figure(figsize=(8,5))
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Artículo")
    plt.ylabel("Numero de figuras")
    plt.savefig("output/figures_per_article.png")
    plt.close()