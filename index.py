import PyPDF2
import re

def get_string_between(string, start, end):
	search = str(start + '(.*)' + end)
	result = re.search(search, string)
	return result.group(1).strip()

pdf_file_obj = open('epc.pdf', 'rb')
epc_pdf = PyPDF2.PdfFileReader(pdf_file_obj)
if epc_pdf.isEncrypted:
	epc_pdf.decrypt("")

epc_page = epc_pdf.getPage(0)
epc_text = epc_page.extractText()

epc_text = epc_text.replace("\n", " ")

result = {}

result["reference number"] = get_string_between(epc_text, "Reference number:", " Date of assessment")
result["address"] = get_string_between(epc_text, "Energy Performance Certificate", "Dwelling")
result["dwelling_type"] = get_string_between(epc_text, "Dwelling type:", "Reference number")
result["assessment"] = get_string_between(epc_text, "Date of assessment:", "Type")
result["floor area"] = get_string_between(epc_text, "Total floor area:", "m²")
result["three year costs"] = get_string_between(epc_text, "costs of dwelling for 3 years: £", "Over 3 years")
result["potential saving"] = get_string_between(epc_text, "Over 3 years you could save £", "Estimated energy")

print(result)