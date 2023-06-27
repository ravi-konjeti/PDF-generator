from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
#print()

df = pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    # this is method of pdf object instance to add pages to a document
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    # RGB color channel to give us output in gray
    pdf.set_text_color(100, 100, 100)
    # 'w' that is width is  always recommended to be zero
    # and 'ln' which is length should be zero
    # 'h' which is height and font should be equal as the border collide if font size increases
    # align is "l" as it is said to be left to the pdf document
    pdf.cell(w=0, h=12,txt=row["Topic"],
             align="L", ln=1)
    # x1,y1 are co-ordinates for starting point of line
    # x2, y2 are co-ordinates for ending point of line
    pdf.line(10,21, 200,21)

    for k in range(31,288,11):
        pdf.line(10,k, 200,k)

    # this is the place we need to print the footer in the pdf. The length from the top
    pdf.ln(265)

    # This is for the footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    # Nested for loop
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for k in range(31, 288, 11):
            pdf.line(10, k, 200, k)
        pdf.ln(277)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")



