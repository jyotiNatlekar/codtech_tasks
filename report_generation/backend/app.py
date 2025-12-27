# Import required libraries
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sqlite3
from report_generator import generate_pdf

# Create Flask app
app = Flask(__name__)
CORS(app)

# Database file name
DB_NAME = "database.db"


# Function to initialize database
def init_db():
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table to store report data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER,
            remarks TEXT
        )
    """)

    # Save changes and close connection
    conn.commit()
    conn.close()


# Call database initialization
init_db()


# API to receive data from frontend
@app.route("/submit", methods=["POST"])
def submit_data():
    # Read JSON data from request
    data = request.json

    name = data["name"]
    score = data["score"]
    remarks = data["remarks"]

    # Insert data into database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reports (name, score, remarks) VALUES (?, ?, ?)",
        (name, score, remarks)
    )
    conn.commit()
    conn.close()

    # Send response to frontend
    return jsonify({"message": "Data stored successfully!"}), 200

# API to generate PDF report
@app.route("/generate-report", methods=["GET"])
def generate_report():
    # Fetch all records from database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, remarks FROM reports")
    data = cursor.fetchall()
    conn.close()

    # Generate PDF using ReportLab
    pdf_path = generate_pdf()

    # Send PDF file to browser
    return send_file(pdf_path, as_attachment=True)


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)
