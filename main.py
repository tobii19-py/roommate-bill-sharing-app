from flat import Bill, Flatmate
from report import PdfReport, FileSharer

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

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
