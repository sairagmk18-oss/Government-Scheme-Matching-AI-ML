import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ai_scores(user, csv_file):

    # Load government schemes
    schemes = pd.read_csv(csv_file)

    # Create a description of the user's requirements
    user_text = f"""
    age {user['age']}
    income {user['income']}
    occupation {user['occupation']}
    category {user['category']}
    gender {user['gender']}
    state {user['state']}
    """

    # Combine scheme information into searchable text
    scheme_text = (
        schemes["scheme_name"].fillna("") + " "
        + schemes["description"].fillna("") + " "
        + schemes["occupation"].fillna("") + " "
        + schemes["category"].fillna("") + " "
        + schemes["gender"].fillna("") + " "
        + schemes["state"].fillna("") + " "
        + schemes["benefits"].fillna("")
    )

    # TF-IDF converts text into numerical vectors
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    all_text = [user_text] + scheme_text.tolist()

    tfidf_matrix = vectorizer.fit_transform(all_text)

    # Compare user profile with every scheme
    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    results = []

    for index, score in enumerate(similarity_scores):

        results.append({
            "scheme_id": schemes.iloc[index]["scheme_id"],
            "scheme_name": schemes.iloc[index]["scheme_name"],
            "ai_score": round(float(score) * 100, 2)
        })

    # Highest AI similarity first
    results.sort(
        key=lambda x: x["ai_score"],
        reverse=True
    )

    return results


# TEST AI MATCHING

if __name__ == "__main__":

    test_user = {

        "age": 20,

        "income": 200000,

        "occupation": "Student",

        "category": "General",

        "gender": "Male",

        "state": "Kerala"
    }

    csv_file = "../data/schemes.csv"

    results = calculate_ai_scores(
        test_user,
        csv_file
    )

    print("\n====================================")
    print("       AI SCHEME MATCHING")
    print("====================================")

    for result in results:

        print(
            result["scheme_name"],
            "→",
            result["ai_score"],
            "%"
        )