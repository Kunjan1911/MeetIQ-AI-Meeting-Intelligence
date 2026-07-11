from collections import Counter
import re

import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop_words = {
    "the","is","a","an","to","of","and","in","for","on","at",
    "we","i","you","our","it","this","that","be","are","was",
    "will","have","has","had","with","as","by","from","or"
}

def generate_wordcloud(text):

    wc = WordCloud(
        width=900,
        height=400,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wc)
    ax.axis("off")

    return fig


def keyword_frequency(text):

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    words = [w for w in words if w not in stop_words]

    counter = Counter(words)

    return counter.most_common(10)