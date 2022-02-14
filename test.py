import pdf2mbox
pdf_file = "test.pdf"
mbox_file = "test.mbox"
# returns dict containing emails
e = pdf2mbox.pdf2mbox(pdf_file, mbox_file)
