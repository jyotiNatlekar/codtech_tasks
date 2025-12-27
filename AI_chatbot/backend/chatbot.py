import spacy
from database import get_db_connection

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Find best matching answer using NLP similarity
def get_best_answer(user_question):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM knowledge")
    rows = cursor.fetchall()

    user_doc = nlp(user_question)

    best_score = 0
    best_answer = None

    for row in rows:
        db_doc = nlp(row["question"])
        similarity = user_doc.similarity(db_doc)

        if similarity > best_score:
            best_score = similarity
            best_answer = row["answer"]

    conn.close()

    # Threshold for similarity
    if best_score > 0.70:
        return best_answer
    else:
        return None

# Save new knowledge to database
def save_knowledge(question, answer):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO knowledge (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()
    conn.close()
