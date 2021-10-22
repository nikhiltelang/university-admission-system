from fpdf import  FPDF
from CassandraOperation import CassandraManagement

class pdf:
    def __init__(self,id):
        self.id = id
        self.cdb = CassandraManagement()

    def pdfwriter(self):
        get_info = self.cdb.student_info(self.id)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, "It's Working", ln=1, align='c')
        pdf.cell(200, 10, "Hello Nikhil", ln=2, align='c')
        return pdf.output("Nikhil.pdf")