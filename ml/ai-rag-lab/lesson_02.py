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


# Each query has document IDs that we have judged relevant.
evaluation_data = [
    {
        "query": "heat transfer",
        "relevant_ids": {3},
    },
    {
        "query": "database and SQL",
        "relevant_ids": {2},
    },
    {
        "query": "machine learning patterns",
        "relevant_ids": {4},
    },
    {
        "query": "heat and temperature",
        "relevant_ids": {1, 3},
    },
]


def retrieve(query, top_k=3):
    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(
        query_vector,
        document_vector,
    )[0]

    # Sort by descending score.
    ranked_indices = scores.argsort()[::-1]

    results = []

    for index in ranked_indices:
        score = float(scores[index])

        # Skip documents with no lexical match.
        if score <= 0:
            continue

        results.append({
            "id": documents[index]["id"],
            "title": documents[index]["title"],
            "score": score,
        })

        if len(results) == top_k:
            break

    return results


def evaluate_query(query, relevant_ids, top_k=3):
    results = retrieve(query, top_k=top_k)

    retrieved_ids = {result["id"] for result in results}
    relevant_found = retrieved_ids & relevant_ids

    precision = (
        len(relevant_found) / len(retrieved_ids)
        if retrieved_ids else 0.0
    )

    recall = (
        len(relevant_found) / len(relevant_ids)
        if relevant_ids else 0.0
    )

    print(f"\nQuery: {query}")
    print("Results:", [r["title"] for r in results])
    print(f"Precision@{top_k}: {precision:.2f}")
    print(f"Recall@{top_k}: {recall:.2f}")


for item in evaluation_data:
    evaluate_query(
        item["query"],
        item["relevant_ids"],
        top_k=3,
    )
