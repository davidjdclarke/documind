import os
import sys
import logging
from load_dotenv import load_dotenv

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
load_dotenv(".env")

from documind.document import Document
from documind.utils import read_file

logger = logging.getLogger(__name__)


FILENAME = "data/ie_report.txt"

if __name__ == "__main__":
    logger.info("Starting test script")
    ie_report = read_file(FILENAME)

    doc = Document(ie_report)

    logger.info(f"Recieved {len(doc.split())} words from document.")
