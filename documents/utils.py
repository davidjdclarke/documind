import json

from typing import Any, List, Optional
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def save_file(file_path: str, data: Any):
    with open(file_path, "w") as f:
        f.write(data)


def save_bytes(file_path: str, data: bytes):
    with open(file_path, "wb") as f:
        f.write(data)


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(file_path: str, data: dict):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def convert_pdf_to_txt(pdf_path):
    resource_manager = PDFResourceManager()
    text_output = StringIO()
    layout_params = LAParams()
    text_converter = TextConverter(
        resource_manager, text_output, laparams=layout_params
    )
    pdf_file = open(pdf_path, "rb")
    pdf_interpreter = PDFPageInterpreter(resource_manager, text_converter)
    password = ""
    max_pages = 0
    caching = True
    page_numbers = set()

    for page in PDFPage.get_pages(
        pdf_file,
        page_numbers,
        maxpages=max_pages,
        password=password,
        caching=caching,
        check_extractable=True,
    ):
        pdf_interpreter.process_page(page)

    extracted_text = text_output.getvalue()

    pdf_file.close()
    text_converter.close()
    text_output.close()
    return extracted_text


def split_list(input_list: List[Any], n: int) -> List[Any]:
    """
    Split a list into n sublists.

    Args:
        input_list (List[Any]): list to split
        n (int): number of sublists

    Returns:
        List[Any]: _description_
    """
    quotient, remainder = divmod(len(input_list), n)
    return [input_list[i * quotient + min(i, remainder):(i + 1) * quotient + min(i + 1, remainder)] for i in range(n)]
