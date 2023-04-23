from langchain.document_loaders import PyPDFLoader
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def read_pdfs():
  files = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "pdfs"))
  pdf_path = os.path.join(Path(Path(__file__).parent).parent, "data", "pdfs", files[0])
  loader = PyPDFLoader(pdf_path)
  pages = loader.load_and_split()
  return pages

