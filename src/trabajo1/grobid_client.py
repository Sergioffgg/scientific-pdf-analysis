import requests
import os
import time

GROBID_URL = os.getenv("GROBID_URL", "http://localhost:8070/api/processFulltextDocument")

def process_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        files = {"input": f}
        r = requests.post(GROBID_URL, files=files) #LLamada API rest grobid
    r.raise_for_status()
    return r.text