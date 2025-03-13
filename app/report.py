from db.database import get_connection, get_recent_scores, get_team_goals, get_team_with_most_goals, get_match_scores, get_event
from .config import load_config
from reportlab.pdfgen import canvas



def report(db, connection):
    teams = input("Enter the team names separated by a comma: ")
    team1, team2 = teams.split(",")

    get_event(db, "HOLD1")
    rows = db.fetchall()

    # Create a new PDF document
    pdf = canvas.Canvas("report.pdf")

    # Write the report title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 750, "Match Report")

    # Write the report content
    pdf.setFont("Helvetica", 12)
    y = 700
    for row in rows:
        pdf.drawString(50, y, "Goals " + row[0])

    # Save the PDF document
    pdf.save()
    