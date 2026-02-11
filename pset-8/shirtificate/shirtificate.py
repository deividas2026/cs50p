from fpdf import FPDF


name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", style="", size=48)
pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.image("shirtificate.png", x=pdf.l_margin, y=70, w=pdf.epw)
pdf.set_font("Helvetica", style="", size=24)
pdf.set_text_color(255)
pdf.cell(0, 140, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
