from src.ocr_func import ocr_pdf, ocr_image
import os

def test_ocr_image():
    image_path = os.path.join("tests", "samples", "ex1.jpg")
    assert 'Shubhayan Sarkar' in ocr_image(image_path)

def test_ocr_pdf():
    pdf_path = os.path.join("tests", "samples", "ex2.pdf")
    assert 'Shubhayan Sarkar' in ocr_pdf(pdf_path)