from werkzeug.datastructures import FileStorage
from transformers import BertForSequenceClassification, BertTokenizer
from src.file_converter import extract_text
import torch

def classify_file(file: FileStorage):

    labels = ["bank_statement", "drivers_licence", "invoice"]
    label2id = {label: i for i, label in enumerate(labels)}
    id2label = {i: label for label, i in label2id.items()}

    model = BertForSequenceClassification.from_pretrained("classifier_model")
    tokenizer = BertTokenizer.from_pretrained("classifier_model/")
    model.eval()

    file_text = extract_text(file)

    inputs = tokenizer(file_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class_id = torch.argmax(outputs.logits, dim=1).item()
    
    return id2label[predicted_class_id]

