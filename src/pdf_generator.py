from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(summary, sentiment, action_items, score):

    file_name = "Meeting_Report.pdf"

    doc = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>MeetSense AI Report</b>", styles["Title"]))

    story.append(Paragraph("<br/><b>Executive Summary</b>", styles["Heading2"]))
    story.append(Paragraph(summary, styles["BodyText"]))

    story.append(Paragraph("<br/><b>Sentiment</b>", styles["Heading2"]))
    story.append(
        Paragraph(
            f"{sentiment['label']} ({round(sentiment['score']*100,2)}%)",
            styles["BodyText"]
        )
    )

    story.append(Paragraph("<br/><b>Productivity Score</b>", styles["Heading2"]))
    story.append(Paragraph(f"{score}/100", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Action Items</b>", styles["Heading2"]))

    for item in action_items:
        story.append(Paragraph("• "+item, styles["BodyText"]))

    doc.build(story)

    return file_name