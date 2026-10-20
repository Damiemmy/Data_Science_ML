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
query = "I need a document about marine introduction biology"

# Step 5: Convert the query using the same vocabulary.
query_vector = vectorizer.transform([query])


# Step 6: Compare the query with each document.
scores = cosine_similarity(
    query_vector,
    document_vectors,
)[0]

# Step 7: Rank documents from highest score to lowest.
ranked_indices = scores.argsort()[::-1]

# Step 8: Display only documents with a positive score.
found_results = False

for index in ranked_indices:
    score = scores[index]

    # Ignore documents with no matching weighted terms.
    if score <= 0:
        continue # continue means Stop executing the remaining lines in this iteration and move to the next item in the loop if condition is met.

    doc = documents[index]

    print(f"{score:.3f} | {doc['title']}")
    found_results = True

# Step 9: Handle queries with no lexical matches.
if not found_results:
    print("No matching documents found.")

# Step 10: Inspect the document matrix.
print("Matrix shape:", document_vectors.shape)
print("Matrix type:", type(document_vectors))


print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nDocument matrix shape:")
print(document_vectors.shape)

queries = [
    "heat transfer",
    "how does heat travel",
    "marine biology",
]

for query in queries:
    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(
        query_vector,
        document_vectors,
    )[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    print(f"\nQuery: {query}")
    print(f"Best score: {best_score:.3f}")

    if best_score == 0:
        print("No lexical match.")
    else:
        print(f"Best document: {documents[best_index]['title']}")
