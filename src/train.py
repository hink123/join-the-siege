from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

dataset = load_dataset("csv", data_files="files/processed_data/generated_text_with_labels.csv", split="train")
dataset = dataset.train_test_split(test_size=0.2)

labels = ["bank_statement", "drivers_licence", "invoice"]
labels_encoded = {label: i for i, label in enumerate(labels)}
labels_encoded_reverse = {i: label for label, i in labels_encoded.items()}

def encode_labels(item):
    item["label"] = labels_encoded[item["label"]]
    return item

dataset = dataset.map(encode_labels)

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize(item):
    return tokenizer(item["text"], padding="max_length", truncation=True, max_length=512)

dataset = dataset.map(tokenize, batched=True)

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=len(labels),
    id2label=labels_encoded_reverse,
    label2id=labels_encoded
)

training_args = TrainingArguments(
    eval_strategy="epoch",
    save_strategy="epoch",
    weight_decay=0.01,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    tokenizer=tokenizer,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

trainer.train()

model.save_pretrained("./classifier_model")
tokenizer.save_pretrained("./classifier_model")