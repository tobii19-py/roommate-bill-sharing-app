import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object containing data about a bill, such as
    total amount and billing period.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate individual who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about
    the flatmates such as names, share and
    billing period
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Insert a title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert the flatmate number 1's name and amount due
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert the flatmate number 2's name and amount due
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


amount = float(input("Hey, enter the bill amount: "))
period = input("What is the billing period? E.g. December 2022: ")

name_1 = input("Please, enter your name? ")
days_in_house_1 = int(input(f"How many days did {name_1} stay in the house during these bill period? "))

name_2 = input("Please, enter your flatmate's name? ")
days_in_house_2 = int(input(f"How many days did {name_2} stay in the house during these bill period? "))

the_bill = Bill(amount, period)
flatmate_1 = Flatmate(name_1, days_in_house_1)
flatmate_2 = Flatmate(name_2, days_in_house_2)

print(f"{flatmate_1.name} pays: ", flatmate_1.pays(the_bill, flatmate_2))
print(f"{flatmate_2.name} pays: ", flatmate_2.pays(the_bill, flatmate_1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate_1, flatmate_2, the_bill)
