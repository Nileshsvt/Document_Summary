from transformers import pipeline
import re

def clean_text(text):
    """
    Cleans the text by removing excessive whitespace, line breaks, and special characters.
    """
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = re.sub(r'[^\w\s.,!?]', '', text)  # Remove non-standard characters
    return text.strip()

def summarize_text(text, max_length=150, min_length=50):
    """
    Summarizes the given text using Hugging Face Transformers.
    Handles long text by splitting it into smaller chunks.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
    max_input_length = 512  # Reduce the input length for better handling

    # Clean the text
    cleaned_text = clean_text(text)

    # Split the text into smaller chunks
    words = cleaned_text.split()
    chunks = [" ".join(words[i:i + max_input_length]) for i in range(0, len(words), max_input_length)]

    # Summarize each chunk and combine the results
    summaries = []
    for i, chunk in enumerate(chunks):
        try:
            summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
            summaries.append(summary)
        except Exception as e:
            print(f"Error summarizing chunk {i + 1}: {e}")
            summaries.append(f"Error summarizing this chunk (chunk {i + 1}).")

    return " ".join(summaries)  # Combine all summaries into a single summary
