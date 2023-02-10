from documind.utils import convert_pdf_to_txt, save_file

PDF_PATH = "data/APPL_10-K-2022.pdf"

pdf_text = convert_pdf_to_txt(PDF_PATH)

save_file("data/APPL_10-K-2022.txt", pdf_text)
