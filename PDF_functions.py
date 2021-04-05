############################################################################
##   Python sample code to create a new pdf file with different formats   ##
##   Author: Gunther Bacellar                                             ##
##   Email: gcbacel@hotmail.com                                           ##
############################################################################

# Steps to run the script:
# 1) install PyPDF3 (python3 -m pip install PyPDF3)
# 2) verify instalation: python3 -m pip show PyPDF3

from PyPDF3 import PdfFileWriter, PdfFileReader
pdf_path = r'C:\Users\gunther\'
input_pdf_name = 'input.pdf'
output_pdf_name = 'output.pdf'
watermark_pdf = 'watermark.pdf'

new_pdf = PdfFileWriter()
with PdfFileReader(open(pdf_path + input_pdf_name, "rb")) as pdf
    # print pdf number of pages
    print("pdf has %d pages." % pdf.getNumPages())

    # add page 1 from pdf readed to the new document, unchanged
    new_pdf .addPage(pdf.getPage(0))

    # add page 2 from pdf readed, but rotated clockwise 90 degrees
    new_pdf .addPage(pdf.getPage(1).rotateClockwise(90))

    # add page 3 from pdf readed, rotated the other way:
    new_pdf.addPage(pdf.getPage(2).rotateCounterClockwise(90))

    # add page 4 from pdf readed, but first add a watermark from another PDF:
    page4 = pdf.getPage(3)
    watermark = PdfFileReader(open(pdf_path + watermark_pdf, "rb"))
    page4.mergePage(watermark.getPage(0))
    new_pdf.addPage(page4)

    # add page 5 from pdf readed, but crop it to half size:
    page5 = pdf.getPage(4)
    page5.mediaBox.upperRight = (
        page5.mediaBox.getUpperRight_x() / 2,
        page5.mediaBox.getUpperRight_y() / 2
    )
    new_pdf.addPage(page5)

    # encrypt your new PDF and add a password
    password = "Brazil"
    new_pdf.encrypt(password)

    # finally, write "output" to document-output.pdf
    outputStream = open(pdf_path + output_pdf_name, "wb")
    new_pdf.write(outputStream)