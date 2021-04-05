############################################################
##   Python sample code to save a html page to pdf        ##
##   Author: Gunther Bacellar                             ##
##   Email: gcbacel@hotmail.com                           ##
############################################################

# Steps to run the script:
# 1) download and install wkhtml from https://wkhtmltopdf.org/downloads.html and get the link for wkhtmltopdf.exe
# 2) install pdfkit python package (pip install pdfkit)

import pdfkit
url = "http://www.google.com"
url = "https://www.seattletimes.com/seattle-news/politics/legislature-passes-bill-that-will-close-northwest-detention-center-in-tacoma/"
path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = path)
pdfkit.from_url(url, "c:\gunther\seattle.pdf", configuration = config)
print(f"pdf successfully created")