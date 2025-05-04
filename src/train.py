from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from constants import INDUSTRIES, INDUSTRIES_ENCODED, INDUSTRIES_DECODED, GENERATED_DATA_LOCATION, MODEL_LOCATION
from datasets import load_dataset

def train_classifier_model():
    dataset = load_dataset("csv", data_files=GENERATED_DATA_LOCATION, split="train")
    dataset = dataset.train_test_split(test_size=0.2)

    def encode_labels(item):
        item["label"] = INDUSTRIES_ENCODED[item["label"]]
        return item

    dataset = dataset.map(encode_labels)

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    def tokenize(item):
        return tokenizer(item["text"], padding="max_length", truncation=True, max_length=512)

    dataset = dataset.map(tokenize, batched=True)

    model = BertForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=len(INDUSTRIES),
        id2label=INDUSTRIES_DECODED,
        label2id=INDUSTRIES_ENCODED
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

    model.save_pretrained(MODEL_LOCATION)
    tokenizer.save_pretrained(MODEL_LOCATION)