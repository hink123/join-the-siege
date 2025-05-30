from datetime import datetime, timedelta
from faker import Faker
from constants import (
    GENERATED_DATA_LOCATION, VEHICLE_TYPES, US_DMV_AGENCIES, 
    US_STATES, TRANSACTION_EXAMPLES, CREDIT_TRANSACTIONS, INVOICE_EXAMPLES
)
import random
import pandas as pd

fake = Faker()

def generate_fake_uk_license():
    name = fake.name()
    first, last = name.split()[0], name.split()[-1]
    dob = fake.date_of_birth().strftime("%d.%m.%Y")
    license_id = f"{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    vehicle = random.choice(VEHICLE_TYPES)
    address = fake.address().replace("\n", ", ")

    text = [
        "DRIVING LICENCE",
        f"1. {last.upper()}",
        f"2. {first.upper()}",
        f"3. {dob} ENGLAND",
        f"4. {license_id} {vehicle} DVLA",
        f"5. {last.upper()} ENG {random.randint(1, 99)}",
        f"6. {first.capitalize()}",
        f"7. {address}",
        f"8. {vehicle.upper()}"
    ]
    return "\n".join(text)

def generate_fake_us_license():
    state = random.choice(US_STATES)
    name = fake.name()
    dob = fake.date_of_birth().strftime("%m/%d/%Y")
    license_num = fake.bothify(text="??######")
    address = fake.address().replace("\n", ", ")
    vehicle = random.choice(VEHICLE_TYPES)
    agency = US_DMV_AGENCIES[state]

    text = [
        f"{state.upper()} DRIVER LICENSE",
        f"Name: {name}",
        f"DOB: {dob}",
        f"License #: {license_num}",
        f"Class: {vehicle}",
        f"Issued by: {agency}",
        f"Address: {address}"
    ]
    return "\n".join(text)


def generate_fake_transaction(date):
    description = random.choice(TRANSACTION_EXAMPLES)
    amount = round(random.uniform(10.00, 700.00), 2)
    is_credit = description in CREDIT_TRANSACTIONS

    return {
        "date": date.strftime("%d/%m/%Y"),
        "description": description,
        "debit": "" if is_credit else f"{amount:.2f}",
        "credit": f"{amount:.2f}" if is_credit else ""
    }

def generate_fake_transaction_text(start_date):
    transactions = []
    text = []

    for _ in range(20):
        random_days = random.randint(0, 27)
        trans_date = start_date + timedelta(days=random_days)
        transactions.append(generate_fake_transaction(trans_date))

    for transaction in transactions:
        text.append(f"{transaction['date']}  {transaction['description']} {transaction['debit']} {transaction['credit']}")
    
    return text

def generate_fake_bank_statement():
    start_year = random.randint(1900, 2025)
    start_month = random.randint(1, 12)
    start_date = datetime.strptime(f"{start_year}-{start_month}-01", "%Y-%m-%d")
    name = fake.name()
    account_number = f"XXXX-XXXX-XXXX-{random.randint(1000, 9999)}"
    transactions_text = generate_fake_transaction_text(start_date)

    text = [
        f"Bank {fake.company()}",
        f"Customer Support: {fake.phone_number()}",
        f"{fake.url()}",
        f"Account Holder: {name}",
        f"Account Number: {account_number}",
        f"Statement Period: {start_year}-{start_month}",
        "",
        "Date Description Debit ($) Credit ($)",
    ]

    text.extend(transactions_text)

    return "\n".join(text)

def generate_invoice_items():
    selected_items = random.sample(INVOICE_EXAMPLES, k=random.randint(2, 4))
    subtotal = 0
    text = []
    for item in selected_items:
        quantity = random.randint(1, 100)
        unit_price = random.randint(1, 1000000)

        total = quantity * unit_price

        subtotal += total
        text.append(f"{item} {quantity} ${unit_price:.2f} ${total:.2f}")

    return (subtotal, text)

def generate_invoice_text():
    invoice_no = random.randint(1000, 9999)
    issue_date = datetime.today().strftime("%d %B %Y")
    due_date = (datetime.today() + timedelta(days=30)).strftime("%d %B %Y")
    
    sender_company = fake.company()
    recipient_name = fake.name()
    recipient_company = fake.company()
    sender_email = fake.company_email()
    sender_phone = fake.phone_number()
    bank_account = fake.bban()
    tax_decimal = random.randint(1, 15)/100
    
    subtotal, invoice_items_text = generate_invoice_items()
    tax = subtotal * tax_decimal
    total = subtotal + tax
    
    text = [
        f"{sender_company} INVOICE",
        f"Issue Date: {issue_date}",
        f"Due Date: {due_date}",
        f"Invoice #: {invoice_no}",
        f"Billed To: {recipient_name} ({recipient_company})",
        "DESCRIPTION QTY UNIT PRICE TOTAL",
    ]

    text += invoice_items_text

    text += [
        f"Subtotal: ${subtotal:.2f}",
        f"Tax ({tax_decimal*100}): ${tax:.2f}",
        f"TOTAL: ${total:.2f}",
        "Payment Info:",
        f"Bank Account: {bank_account}",
        f"Email: {sender_email}",
        f"Phone: {sender_phone}",
        "Please make payment within 30 days."
    ]

    return "\n".join(text)


def generate_fake_data():
    fake_data = []
    for _ in range(100):
        licensce_text_uk = generate_fake_uk_license()
        fake_data.append({"text": licensce_text_uk, "label": "drivers_licence"})

        licensce_text_us = generate_fake_us_license()
        fake_data.append({"text": licensce_text_us, "label": "drivers_licence"})

        bank_statement_text = generate_fake_bank_statement()
        fake_data.append({"text": bank_statement_text, "label": "bank_statement"})

        invoice_text = generate_invoice_text()
        fake_data.append({"text": invoice_text, "label": "invoice"})

    pd.DataFrame(fake_data).to_csv(GENERATED_DATA_LOCATION, index=False)
