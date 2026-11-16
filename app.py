from flask import Flask, render_template, request

from models.matcher import find_schemes
from models.ai_matcher import calculate_ai_scores


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    # Get user information


    user = {
        "age": int(request.form["age"]),
        "income": int(request.form["income"]),
        "occupation": request.form["occupation"],
        "category": request.form["category"],
        "gender": request.form["gender"],
        "state": request.form["state"]
    }

    csv_file = "data/schemes.csv"

    # Rule-based eligibility

    eligibility_results = find_schemes(
        user,
        csv_file
    )

    # AI matching

    ai_results = calculate_ai_scores(
        user,
        csv_file
    )

    # Create AI score dictionary
    ai_scores = {
        item["scheme_id"]: item["ai_score"]
        for item in ai_results
    }

    # Combine both scores

    final_results = []

    for result in eligibility_results:

        scheme_id = result["scheme_id"]

        eligibility_score = result["score"]

        ai_score = ai_scores.get(
            scheme_id,
            0
        )

        final_score = (
            eligibility_score * 0.70
            + ai_score * 0.30
        )

        # Determine recommendation

        if result["eligible"]:

            status = "Highly Eligible"

        elif final_score >= 70:

            status = "Possibly Eligible"

        else:

            status = "Not Eligible"

        final_results.append({

            "scheme_id": scheme_id,

            "scheme_name": result["scheme_name"],

            "description": result["description"],

            "eligibility_score": eligibility_score,

            "ai_score": ai_score,

            "final_score": round(
                final_score,
                2
            ),

            "eligible": result["eligible"],

            "status": status,

            "reasons": result["reasons"],

            "benefits": result["benefits"]

        })

    # Sort by final score

    final_results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return render_template(
        "results.html",
        results=final_results
    )


if __name__ == "__main__":

    app.run(debug=True)