from sklearn.feature_extraction.text import TfidfVectorizer

def extract_key_points(text, num_points=5):
    """Extracts key points from the text using TF-IDF."""
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    vectorizer = TfidfVectorizer(stop_words='english')

    try:
        X = vectorizer.fit_transform(sentences)
        scores = X.sum(axis=1).tolist()
        key_points = sorted(
            [(sentences[i], scores[i][0]) for i in range(len(sentences))],
            key=lambda x: x[1], reverse=True
        )
        return [kp[0] for kp in key_points[:num_points]]
    except Exception as e:
        print(f"Error extracting key points: {str(e)}")
        return ["Error extracting key points."]
