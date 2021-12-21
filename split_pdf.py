from PyPDF2 import PdfFileWriter, PdfFileReader
import os

os.chdir("./split")

inputpdf = PdfFileReader(open("input.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)