from textblob import TextBlob

def analizar_sentimiento(texto):
    if not texto:
        return 'Neutral'
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    if polaridad > 0.1:
        return 'Positivo'
    elif polaridad < -0.1:
        return 'Negativo'
    else:
        return 'Neutral'