from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    {
        "id": 1,
        "title": "Introduction to Thermodynamics",
        "content": "Thermodynamics studies heat, temperature, energy, and work.",
    },
    {
        "id": 2,
        "title": "Database Management Systems",
        "content": "Database systems organize data using tables, SQL, and relationships.",
    },
    {
        "id": 3,
        "title": "Heat Transfer Fundamentals",
        "content": "Heat transfer explains how thermal energy moves between objects.",
    },
    {
        "id": 4,
        "title": "Introduction to Machine Learning",
        "content": "Machine learning uses data to learn patterns and make predictions.",
    },
]

texts=[
    f"{doc['title']} {doc['content']}" for doc in documents
]

vectorizer = TfidfVectorizer()
document_vector = vectorizer.fit_transform(texts)
query='i need a machine learning material'
query_vector=vectorizer.transform([query])

scores= cosine_similarity(
    query_vector,
    document_vector,
)

ranked_indicies=scores.argsort()[::-1]

for index in ranked_indicies:
    doc=scores[index]
    score=scores[]
print(ranked_indicies)