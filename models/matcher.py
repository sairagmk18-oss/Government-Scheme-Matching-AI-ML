import pandas as pd


def check_eligibility(user, scheme):
    """
    Check all available eligibility conditions
    for one government scheme.
    """

    conditions = []
    reasons = []

    # 1. AGE

    age_match = (
        user["age"] >= int(scheme["min_age"])
        and user["age"] <= int(scheme["max_age"])
    )

    conditions.append(age_match)

    if age_match:
        reasons.append("Age requirement satisfied")
    else:
        reasons.append("Age requirement not satisfied")

    # 2. INCOME

    income_match = user["income"] <= int(scheme["max_income"])

    conditions.append(income_match)

    if income_match:
        reasons.append("Income requirement satisfied")
    else:
        reasons.append("Income exceeds the limit")

    # 3. OCCUPATION

    scheme_occupation = str(scheme["occupation"]).strip().lower()
    user_occupation = str(user["occupation"]).strip().lower()

    occupation_match = (
        scheme_occupation == "any"
        or scheme_occupation == user_occupation
    )

    conditions.append(occupation_match)

    if occupation_match:
        reasons.append("Occupation requirement satisfied")
    else:
        reasons.append("Occupation requirement not satisfied")

    # 4. CATEGORY

    scheme_category = str(scheme["category"]).strip().lower()
    user_category = str(user["category"]).strip().lower()

    category_match = (
        scheme_category == "all"
        or scheme_category == user_category
    )

    conditions.append(category_match)

    if category_match:
        reasons.append("Category requirement satisfied")
    else:
        reasons.append("Category requirement not satisfied")

    # 5. GENDER

    scheme_gender = str(scheme["gender"]).strip().lower()
    user_gender = str(user["gender"]).strip().lower()

    gender_match = (
        scheme_gender == "all"
        or scheme_gender == user_gender
    )

    conditions.append(gender_match)

    if gender_match:
        reasons.append("Gender requirement satisfied")
    else:
        reasons.append("Gender requirement not satisfied")

    # 6. STATE

    scheme_state = str(scheme["state"]).strip().lower()
    user_state = str(user["state"]).strip().lower()

    state_match = (
        scheme_state == "all"
        or scheme_state == user_state
    )

    conditions.append(state_match)

    if state_match:
        reasons.append("State requirement satisfied")
    else:
        reasons.append("State requirement not satisfied")

    # CALCULATE SCORE

    total_conditions = len(conditions)

    satisfied_conditions = sum(conditions)

    score = (
        satisfied_conditions / total_conditions
    ) * 100

    # FINAL RESULT

    return {
        "score": round(score, 2),
        "eligible": all(conditions),
        "reasons": reasons
    }


def find_schemes(user, csv_file):

    schemes = pd.read_csv(csv_file)

    results = []

    for _, scheme in schemes.iterrows():

        result = check_eligibility(user, scheme)

        results.append({
            "scheme_id": scheme["scheme_id"],
            "scheme_name": scheme["scheme_name"],
            "description": scheme["description"],
            "score": result["score"],
            "eligible": result["eligible"],
            "reasons": result["reasons"],
            "benefits": scheme["benefits"]
        })

    # Highest score first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


# TEST THE ELIGIBILITY ENGINE

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

    results = find_schemes(
        test_user,
        csv_file
    )

    print("\n====================================")
    print(" GOVERNMENT SCHEME RECOMMENDATIONS")
    print("====================================")

    for result in results:

        print("\n------------------------------------")

        print(
            "Scheme:",
            result["scheme_name"]
        )

        print(
            "Score:",
            result["score"],
            "%"
        )

        print(
            "Eligible:",
            result["eligible"]
        )

        print(
            "Benefits:",
            result["benefits"]
        )

        print("Reasons:")

        for reason in result["reasons"]:

            print(
                " -",
                reason
            )