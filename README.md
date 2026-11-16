# Government Scheme Matching and Eligibility Intelligence System

## Project Overview

The Government Scheme Matching and Eligibility Intelligence System is an AI/ML-based web application developed using Python and Flask.

The main objective is to help users identify government schemes that may match their personal information, such as age, income, occupation, category, gender and state.

The system combines rule-based eligibility checking with AI-based text similarity to rank relevant government schemes.

## Problem Statement

Many people are unaware of government schemes and find it difficult to identify schemes for which they may qualify.

This project aims to simplify the process by providing an intelligent platform that matches user information with available scheme criteria.

## Objectives

- Identify potentially eligible government schemes.
- Collect user details through a web form.
- Apply rule-based eligibility checking.
- Use AI techniques to measure scheme relevance.
- Rank schemes based on combined scores.
- Display results with explanations.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Flask | Backend web framework |
| HTML | Frontend structure |
| CSS | Frontend styling |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Scikit-learn | AI and text similarity |
| CSV | Scheme dataset storage |

## AI and ML Techniques

### 1. Rule-Based Matching
Uses predefined conditions to check age, income, occupation, category, gender and state.

### 2. TF-IDF
Term Frequency–Inverse Document Frequency converts text into numerical vectors based on word importance.

### 3. Cosine Similarity
Measures the similarity between user information and government scheme descriptions.

### 4. Weighted Scoring

The final recommendation score is calculated using:

Final Score = (Eligibility Score × 70%) + (AI Score × 30%)

## Project Structure

```text
Government-Scheme-Matching-AI-ML/
│
├── app.py
├── data/
│   └── schemes.csv
├── models/
│   ├── matcher.py
│   └── ai_matcher.py
├── templates/
│   ├── index.html
│   └── results.html
└── .gitignore
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/sairagmk18-oss/Government-Scheme-Matching-AI-ML.git
```

### Step 2: Open the Project Folder

```bash
cd Government-Scheme-Matching-AI-ML
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open in Browser

```text
http://127.0.0.1:5000
```

## How the System Works

1. User opens the web application.
2. User enters personal information.
3. The backend processes the submitted information.
4. The rule-based engine checks eligibility conditions.
5. The AI module calculates text similarity using TF-IDF and cosine similarity.
6. The system calculates the final recommendation score.
7. Results are displayed in ranked order.

## Future Enhancements

- Integration with verified government scheme databases.
- Addition of more government schemes.
- Improved AI-based recommendation techniques.
- User authentication and profile management.
- Database integration.
- Deployment as a public web application.

## Important Note

This is an academic prototype. The included scheme dataset contains sample records. Eligibility results should not be treated as official government approval.

## Author

**Sairag MK**

AI and ML Academic Project

## License

This project is developed for educational purposes.
