from fastapi import FastAPI, File, UploadFile, Query
from src.ocr_func import ocr_image, ocr_pdf
import tempfile
from pathlib import Path


# mode = "image"
# # file_path = input("Enter path to the file: ").strip()
# # print(os.listdir())
# file_path = r"tests/samples/ex1.jpg"

# if mode == "image" and os.path.isfile(file_path):
#     text = ocr_image(file_path)
#     print("🖼️ Extracted Text from Image:\n", text)

# elif mode == "pdf" and os.path.isfile(file_path):
#     text = ocr_pdf(file_path)
#     print("📄 Extracted Text from PDF:\n", text)

# else:
#     print("❌ Invalid mode or file path.")




app = FastAPI()
@app.get("/")
async def home():
    return "status ok"

@app.post("/process_file")
async def process_file(file: UploadFile = File(..., description="Upload a CSV or Excel file")):
    """
    Accepts a file, reads its content as text, and returns the text.
    """
    # doc = BytesIO(file.file.read())
    # doc = doc.getvalue()
    # print(doc)
    image_bytes = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix, mode='wb') as temp_file:
        temp_file.write(image_bytes)
        saved_path = temp_file.name
    # print(saved_path)


    if file.filename.endswith((".jpg", ".jpeg", ".JPEG")):
        text = ocr_image(saved_path)
    elif file.filename.endswith(".pdf"):
        text = ocr_pdf(saved_path)
    else:
        return "invalid format"
    
    
    
    return text