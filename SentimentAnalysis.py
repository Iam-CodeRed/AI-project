from textblob import TextBlob

# Taking user input
text = input("Enter a sentence: ")

# Determining the Polarity 
polarity = TextBlob(text).sentiment.polarity

def interpret_polarity(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

print("\nSentiment Analysis Result:")
print("Polarity:", interpret_polarity(polarity))