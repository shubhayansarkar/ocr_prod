from src.ocr_func import ocr_pdf, ocr_image

def test_ocr_image():
    assert 'Shubhayan Sarkar' in ocr_image(r"tests/samples/ex1.jpg")

def test_ocr_pdf():
    assert 'Shubhayan Sarkar' in ocr_pdf(r'tests/samples/ex2.pdf')