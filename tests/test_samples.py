from src.ocr_func import ocr_pdf, ocr_image
import os

def test_ocr_image():
    image_path = os.path.join("tests", "samples", "ex1.jpg")
    assert ocr_image(image_path) == 'Shubhayan Sarkar'

def test_ocr_pdf():
    pdf_path = os.path.join("tests", "samples", "ex2.pdf")
    assert ocr_pdf(pdf_path) == 'Shubhayan Sarkar'