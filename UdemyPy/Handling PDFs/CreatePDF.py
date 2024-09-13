from fpdf import FPDF
import pandas
import fitz    # Package PyMuPdf
import tabula    # Package tabula-py


def create_simple_pdf(pdf):
    pdf.add_page()

    pdf.image('Plan.jpg', w=455, h=256)

    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt="Why So Serious!!!", align='C', border=1, ln=1)

    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=0, h=25, txt='Description', ln=1)

    pdf.set_font(family='Times', size=12)
    txt1 = """
    Joker is a 2019 American psychological thriller film[4] directed and co-produced by Todd Phillips from a screenplay he wrote with Scott Silver. The film, loosely based on DC Comics characters, stars Joaquin Phoenix as the Joker. Set in 1981, it follows Arthur Fleck, a failed clown and aspiring stand-up comedian whose descent into mental illness and nihilism inspires a violent countercultural revolution against the wealthy in a decaying Gotham City. Robert De Niro, Zazie Beetz, and Frances Conroy appear in supporting roles. Distributed by Warner Bros. Pictures, Joker was produced by Warner Bros. Pictures and DC Films in association with Village Roadshow Pictures, Bron Creative and Joint Effort.
    """
    pdf.multi_cell(w=0, h=25, txt=txt1)

    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt='Directed by')

    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=25, txt='Todd Phillips', ln=1)

    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt='Written by')

    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=25, txt='Scott Silver', ln=1)

    pdf.output('Output.pdf')


def create_pdfs_from_excel(pdf):
    df = pandas.read_excel('data.xlsx')

    for index, row in df.iterrows():
        # pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=50, txt=row['Name'], align='C', ln=1)

        for column in df.columns[1:]:
            pdf.set_font(family='Times', style='B', size=14)
            pdf.cell(w=100, h=25, txt=f"{column.title()}:")

            pdf.set_font(family='Times', size=14)
            pdf.cell(w=100, h=25, txt=row[column], ln=1)

        pdf.output(f"{row['Name']}.pdf")


def extract_text_from_pdf():
    with fitz.open("OS10882696_EBI.pdf") as pdf:
        # pdf[0].get_text()
        text = ''
        for page in pdf:
            text = text + page.get_text()


def extract_table_from_pdf():
    table = tabula.read_pdf('OS10882696_EBI.pdf', pages=3)
    table[0].to_excel('output.xlsx', index=None)


def main():
    pdf = FPDF(orientation='P', unit='pt', format='A4')

    # create_simple_pdf(pdf)
    # create_pdfs_from_excel(pdf)
    # extract_text_from_pdf()
    extract_table_from_pdf()


if __name__ == '__main__':
    main()
