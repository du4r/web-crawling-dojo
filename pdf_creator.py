from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(text,path):
    
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    c.setTitle("VAGAS")

    c.drawString(100, height - 100, text)

    c.save()

    print(f"PDF criado com sucesso e salvo em {path}")
