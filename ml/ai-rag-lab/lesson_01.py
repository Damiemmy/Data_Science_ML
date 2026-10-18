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

# Step 1: Build the text collection.
texts = [
    f"{doc['title']} {doc['content']}"
    for doc in documents
]
    #note: there are same solutions
'''
    texts = []

    for doc in documents:
        combined_text = f"{doc['title']} {doc['content']}"
        texts.append(combined_text)
'''

# Step 2: Create the vectorizer.
vectorizer = TfidfVectorizer()

# Step 3: Learn the vocabulary and vectorize documents.
document_vectors = vectorizer.fit_transform(texts)

# Step 4: Accept a student's question.
query = "I need a document about marine biology"

# Step 5: Convert the query using the same vocabulary.
query_vector = vectorizer.transform([query])

# Step 6: Compare the query with each document.
scores = cosine_similarity(
    query_vector,
    document_vectors,
)[0]

# Step 7: Rank the documents.
ranked_indices = scores.argsort()[::-1]

# Step 8: Display the best matches.
for index in ranked_indices:
    doc = documents[index]
    

    print(f" {doc['title']}")

print(document_vectors.shape)
print(type(document_vectors))
