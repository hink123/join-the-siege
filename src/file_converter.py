from pypdf import PdfReader
from werkzeug.datastructures import FileStorage
from src.constants import IMAGE_TYPES
import os
import pytesseract
import cv2
import numpy

def extract_text_from_pdf(file: FileStorage):
    reader = PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages])

def preprocess_image(file: FileStorage):
    image = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)

    resized_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    grayed_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    filtered_image = cv2.bilateralFilter(grayed_image, 11, 17, 17)

    _, threshed_image = cv2.threshold(filtered_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return threshed_image

def extract_text_from_image(file: FileStorage):
    image = preprocess_image(file)
    return pytesseract.image_to_string(image)

def extract_text(file: FileStorage):
    text = None
    file_type = file.filename.split(".")[-1].lower()

    if file_type in IMAGE_TYPES:
        text = extract_text_from_image(file)

    if file_type == "pdf":
        text = extract_text_from_pdf(file)

    return text
