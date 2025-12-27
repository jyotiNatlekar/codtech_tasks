from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import sqlite3
import os

def generate_pdf():
    pdf_path = "report.pdf"

    if os.path.exists(pdf_path):
        os.remove(pdf_path)

    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    # ===== TITLE =====
    content.append(Paragraph("<b>STUDENT MARKSHEET</b>", styles["Title"]))
    content.append(Paragraph("<br/>", styles["Normal"]))

    # ===== DB FETCH =====
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, remarks FROM reports")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        content.append(Paragraph("No records found.", styles["Normal"]))
    else:
        name, score, remarks = rows[-1]

        # ===== MARKSHEET TABLE =====
        table_data = [
            ["Student Name", name],
            ["Marks Obtained", score],
            ["Maximum Marks", "100"],
            ["Result", "PASS" if int(score) >= 40 else "FAIL"],
            ["Remarks", remarks]
        ]

        table = Table(table_data, colWidths=[200, 250])

        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONT", (0, 0), (-1, -1), "Helvetica"),
            ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("PADDING", (0, 0), (-1, -1), 10),
        ]))

        content.append(table)

        content.append(Paragraph("<br/><br/>", styles["Normal"]))
        content.append(Paragraph("Signature of Examiner", styles["Normal"]))

    doc.build(content)
    return pdf_path
