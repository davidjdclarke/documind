from documents.utils import convert_pdf_to_txt, save_file

PDF_PATH = "data/David Clarke - AI Developer.pdf"

pdf_text = convert_pdf_to_txt(PDF_PATH)

save_file("data/resume.txt", pdf_text)
