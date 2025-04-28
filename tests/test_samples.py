from src.ocr_func import ocr_pdf, ocr_image

def test_ocr_image():
    assert ocr_image(r"tests\samples\IMG_20250401_144638487.jpg") == 'Shubhayan Sarkar'

def test_ocr_pdf():
    assert ocr_pdf(r'test\samples\ex2.pdf') == 'Shubhayan Sarkar'