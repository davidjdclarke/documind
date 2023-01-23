import pytest
import os
import sys
from load_dotenv import load_dotenv

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
load_dotenv(".env")

from documents.utils import write_text_file, read_text_file, convert_pdf_to_txt


def test_convert_pdf_to_txt_with_valid_file():
    pdf_file = "tests/resources/APPL_10-K-2022.pdf"
    expected_output = read_text_file("tests/resources/outputs/APPL_10-K-2022.txt")
    output = convert_pdf_to_txt(pdf_file)
    # write_text_file("tests/resources/outputs/APPL_10-K-2022.txt", output)
    assert output == expected_output


def test_convert_pdf_to_txt_with_invalid_file():
    pdf_file = "non_existent.pdf"
    with pytest.raises(FileNotFoundError):
        convert_pdf_to_txt(pdf_file)
