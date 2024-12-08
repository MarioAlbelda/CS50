from fpdf import FPDF, Align, XPos, YPos
from PIL import Image

pdf = FPDF()
pdf.add_page()

name = input("Name: ")

# writting 'CS50 Shirtificate' on the top of the page
pdf.set_font("helvetica", "B", 25)
pdf.cell(0, 10, 'CS50 Shirtificate', align='C', new_y=YPos.NEXT)

# printing the t-shirt image on the page centered horizontally
pdf.ln(10)
pdf.image("shirtificate.png", x= Align.C, y = None)

# printing message with user's name
width, height = Image.open("shirtificate.png").size
pdf.set_y(pdf.get_y()-(height*3/4))
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, name + ' took CS50', align='C')

# saving the pdf
pdf.output("shirtificate.pdf")
