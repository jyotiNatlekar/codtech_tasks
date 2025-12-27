import os
import sqlite3

def get_db_connection():
    """
    Creates and returns a connection to the SQLite database
    using an absolute path so it works from any directory.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "chatbot.db")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """
    Creates the knowledge table if it does not already exist.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_default_knowledge():
    """
    Insert predefined questions and answers
    so the chatbot already knows things.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    default_data = [
        ("What is AI?", "AI stands for Artificial Intelligence. It allows machines to think like humans."),
        ("What is Python?", "Python is a popular programming language used for AI, web development, and automation."),
        ("What is NLP?", "NLP stands for Natural Language Processing. It helps computers understand human language."),
        ("Who developed Python?", "Python was developed by Guido van Rossum."),
        ("What is machine learning?", "Machine learning is a subset of AI that allows systems to learn from data."),
        ("What is Flask?", "Flask is a lightweight Python web framework."),
    ]

    for question, answer in default_data:
        cursor.execute(
            "INSERT INTO knowledge (question, answer) VALUES (?, ?)",
            (question, answer)
        )

    conn.commit()
    conn.close()
