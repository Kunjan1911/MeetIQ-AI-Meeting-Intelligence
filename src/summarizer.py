from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_summary(transcript):

    if len(transcript) < 50:
        return transcript

    max_chunk = 900

    chunks = []

    for i in range(0, len(transcript), max_chunk):
        chunks.append(transcript[i:i+max_chunk])

    final_summary = ""

    for chunk in chunks:

        summary = summarizer(
            chunk,
            max_length=120,
            min_length=40,
            do_sample=False
        )[0]["summary_text"]

        final_summary += summary + "\n\n"

    return final_summary