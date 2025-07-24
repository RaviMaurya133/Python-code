import PyPDF2

pdf_merger = PyPDF2.PdfMerger()

# Ask for number of PDFs to merge
n = int(input("How many PDF files do you want to merge: "))

for i in range(n):
    file_path = input(f"Enter path for PDF file {i + 1}: ").strip()
    pdf_merger.append(file_path)

# Save the merged file
output = input("Enter name for output file: ").strip()
pdf_merger.write(output)
pdf_merger.close()

print("PDFs merged successfully.")
