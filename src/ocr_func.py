import base64
from io import BytesIO
import fitz
from PIL import Image
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Groq client
client = Groq()

# def encode_image(image: Image.Image) -> str:
#     """Convert a PIL image to base64 encoded string"""
#     buffered = BytesIO()
#     image.save(buffered, format="JPEG")
#     return base64.b64encode(buffered.getvalue()).decode("utf-8")
def encode_image(image_bytes):
    """Encodes raw image bytes to base64 string."""
    return base64.b64encode(image_bytes).decode('utf-8')

def ocr_image(image_path):
    """OCR for a single image using Groq API"""
    # image = Image.open(image_path)
    with open(image_path, "rb") as f:
        img_bytes = f.read()
    encoded_image = encode_image(img_bytes)

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract all text from this image."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content


def ocr_pdf(pdf_path):
    """OCR for each page in a PDF using Groq API, using fitz instead of convert_from_path."""
    doc = fitz.open(pdf_path)
    extracted_text = ""

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        pix = page.get_pixmap(dpi=200)  # render page at 200 DPI
        img_bytes = pix.tobytes("jpeg")  # get JPEG bytes

        encoded_image = encode_image(img_bytes)

        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"Extract all text from page {page_number + 1}."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ]
                }
            ]
        )

        extracted_text += f"\n--- Page {page_number + 1} ---\n"
        extracted_text += response.choices[0].message.content

    return extracted_text


# ---------- Example usage ----------

# Change these paths based on what you want to process:
# image_path = "example.jpg"
# pdf_path = "example.pdf"

# mode = input("Enter mode (image/pdf): ").strip().lower()
# mode = "image"
# # file_path = input("Enter path to the file: ").strip()
# file_path = r"tests\samples\ex1.jpg"

# if mode == "image" and os.path.isfile(file_path):
#     text = ocr_image(file_path)
#     print("🖼️ Extracted Text from Image:\n", text)

# elif mode == "pdf" and os.path.isfile(file_path):
#     text = ocr_pdf(file_path)
#     print("📄 Extracted Text from PDF:\n", text)

# else:
#     print("❌ Invalid mode or file path.")