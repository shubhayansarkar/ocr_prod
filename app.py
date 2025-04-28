from src.ocr_func import ocr_image, ocr_pdf
import os
mode = "image"
# file_path = input("Enter path to the file: ").strip()
file_path = r"tests\samples\ex1.jpg"

if mode == "image" and os.path.isfile(file_path):
    text = ocr_image(file_path)
    print("🖼️ Extracted Text from Image:\n", text)

elif mode == "pdf" and os.path.isfile(file_path):
    text = ocr_pdf(file_path)
    print("📄 Extracted Text from PDF:\n", text)

else:
    print("❌ Invalid mode or file path.")