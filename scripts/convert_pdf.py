import os
import io
import load_dotenv

import pandas as pd

from documents.utils import convert_pdf_to_txt, save_file
from documents.openai import OpenAIConnector
from documents.prompt import Prompt


# Load the environment variables
# load_dotenv(".env")
# OPENAI_API_KEY = "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"

PDF_PATH = "data/David Clarke - AI Developer.pdf"

# openai = OpenAIConnector(OPENAI_API_KEY)

pdf_text = convert_pdf_to_txt(PDF_PATH)

# data = openai.complete(
#     Prompt.format_question_prompt(
#         text=pdf_text,
#         promt="convert the costs to csv (don't include commas in the numbers)",
#     ),
#     max_tokens=100,
# )
save_file("data/resume.txt", pdf_text)

# df = pd.read_csv("tmp/invoice.csv")
# df.to_csv("tmp/invoice2.csv", index=False)
