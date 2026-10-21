#EMBEDDINGS
from sentence_transformers import SentenceTransformer
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

# 1. Load a pretrained embedding model.
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Combine each title and its content.
texts = [
    f"{doc['title']}. {doc['content']}"
    for doc in documents
]

# 3. Convert every document into an embedding.
document_embeddings = model.encode(
    texts,
    normalize_embeddings=True,
)

# 4. Enter a question using different wording.
query = "How do computer learn from data?"

# 5. Convert the question into an embedding.
query_embedding = model.encode(
    [query],
    normalize_embeddings=True,
)

# 6. Compare the query with the document embeddings.
scores = cosine_similarity(
    query_embedding,
    document_embeddings,
)[0]

# 7. Rank and display the results.
ranked_indices = scores.argsort()[::-1]

for index in ranked_indices:
    doc = documents[index]
    score = scores[index]

    print(f"{score:.3f} | {doc['title']}")
