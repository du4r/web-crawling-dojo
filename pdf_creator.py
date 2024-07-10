from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet    
import os

def create_pdf(text,path):
    
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    c.setTitle("VAGAS")

    margin = 16
    x_position = margin
    y_position = height - 2 * margin
    
    max_width = width - 2 * margin
    line_spacing = 12
    
    words = text.split()
    
    current_line = ""
    
    for word in words:

        if c.stringWidth(current_line + word + " ", "Helvetica", 12) <= max_width:
            current_line += word + " "
        else:
            c.drawString(x_position, y_position, current_line)
            y_position -= line_spacing
            current_line = word + " "
            
            if y_position < margin:
                c.showPage()
                y_position = height - margin

    if current_line:
        c.drawString(x_position, y_position, current_line)

    c.save()

    print(f"PDF criado com sucesso e salvo em {path}")
