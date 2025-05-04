from werkzeug.datastructures import FileStorage
from transformers import BertForSequenceClassification, BertTokenizer
from src.file_converter import extract_text
from src.constants import INDUSTRIES_DECODED, MODEL_LOCATION
import torch

def classify_file(file: FileStorage):

    model = BertForSequenceClassification.from_pretrained(MODEL_LOCATION)
    tokenizer = BertTokenizer.from_pretrained(MODEL_LOCATION)
    model.eval()

    file_text = extract_text(file)

    inputs = tokenizer(file_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class_id = torch.argmax(outputs.logits, dim=1).item()
    
    return INDUSTRIES_DECODED[predicted_class_id]

