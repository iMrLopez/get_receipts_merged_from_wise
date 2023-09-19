import requests
from pathlib import Path
import PyPDF2, os

TW_TOKEN = "<SET_ME>"
TW_API_URL = f"https://api.transferwise.com/v1/transfers/<transfer_id>/receipt.pdf"

headers = {'Authorization': f"Bearer {TW_TOKEN}"}

data = {
    "MARNY LOPEZ": [11111111, 222222222],
}

print("--- GETTING ALL RECEIPTS FOR PAYEES IN data DICT and merging by PAYEE")
receipts_merged_by_payee = []
for payee in data:
    payee_path = f"output/{payee}"
    os.mkdir(payee_path)
    print(f"Getting {len(data[payee])} receipts for {payee}")
    mergedFile = PyPDF2.PdfMerger()

    for index, transfer_id in enumerate(data[payee]):
        pdf = requests.get(TW_API_URL.replace("<transfer_id>",f"{transfer_id}"), headers=headers)

        if pdf.status_code == 200:
            pdf_path = f'{payee_path}/{payee}_{index}.pdf'
            Path(pdf_path).write_bytes(pdf.content)
            mergedFile.append(PyPDF2.PdfReader(pdf_path, 'rb'))
        else:
            print(f"Failed to get {transfer_id} for {payee}, status_code: {pdf.status_code}")
    merged_path = f"{payee_path}/{payee}_receipts.pdf"
    receipts_merged_by_payee.append(merged_path) # add to global array for final merging
    mergedFile.write(merged_path)

print (f"--- MERGING ALL RECEIPTS TOGETHER ---")
mergedFile = PyPDF2.PdfMerger()
for merged_receipts_path in receipts_merged_by_payee:
    mergedFile.append(PyPDF2.PdfReader(merged_receipts_path, 'rb'))
mergedFile.write(f"output/all_receipts.pdf")


