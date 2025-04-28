from src.ocr_func import ocr_pdf, ocr_image

def test_ocr_image():
    assert ocr_image(r"ocr_mlops\tests\samples\ex1.jpg") == 'Shubhayan Sarkar'

def test_ocr_pdf():
    assert ocr_pdf(r'ocr_mlops\tests\samples\ex2.pdf') == 'Shubhayan Sarkar'