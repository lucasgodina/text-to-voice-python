"""
La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz.
"""

from newspaper import Article
from gtts import gTTS
import nltk

# Descargar los recursos necesarios de nltk
nltk.download("punkt")
nltk.download("punkt_tab")


def article_to_mp3(url, output_file):
    # Extraer el artículo
    article = Article(url, language="es")
    article.download()
    article.parse()
    article.nlp()
    text = article.text

    # Convertir el texto a voz
    tts = gTTS(text=text, lang="es")
    tts.save(output_file)
    print(f"Archivo de audio guardado como {output_file}")


if __name__ == "__main__":
    url = input("Introduce la URL del artículo: ")
    output_file = "articulo.mp3"
    article_to_mp3(url, output_file)
