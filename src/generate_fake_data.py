from faker import Faker
from datetime import datetime, timedelta
import random
import pandas as pd
import os


CSV_PATH = os.path.join("files/processed_data/", "generated_text_with_labels.csv")
fake = Faker()

us_states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

vehicle_types = ["Motorcycle", "Car", "Commercial Vehicle", "3 Wheeler Only"]
dmv_agencies = {
    "Alabama": "Department of Public Safety (DPS)",
    "Alaska": "Division of Motor Vehicles (DMV)",
    "Arizona": "Motor Vehicle Division (MVD)",
    "Arkansas": "Office of Motor Vehicle (OMV)",
    "California": "Department of Motor Vehicles (DMV)",
    "Colorado": "Division of Motor Vehicles (DMV)",
    "Connecticut": "Department of Motor Vehicles (DMV)",
    "Delaware": "Division of Motor Vehicles (DMV)",
    "Florida": "Department of Highway Safety and Motor Vehicles (DHSMV)",
    "Georgia": "Department of Driver Services (DDS)",
    "Hawaii": "County-level Motor Vehicle Offices",
    "Idaho": "Division of Motor Vehicles",
    "Illinois": "Driver Services Department (for licenses), Vehicle Services Department (for vehicle records)",
    "Indiana": "Bureau of Motor Vehicles (BMV)",
    "Iowa": "Department of Transportation (DOT)",
    "Kansas": "Department of Revenue – Division of Vehicles",
    "Kentucky": "Transportation Cabinet – Division of Driver Licensing",
    "Louisiana": "Office of Motor Vehicles (OMV)",
    "Maine": "Bureau of Motor Vehicles (BMV)",
    "Maryland": "Motor Vehicle Administration (MVA)",
    "Massachusetts": "Registry of Motor Vehicles (RMV)",
    "Michigan": "Secretary of State (SOS)",
    "Minnesota": "Driver and Vehicle Services (DVS)",
    "Mississippi": "Department of Public Safety (DPS)",
    "Missouri": "Department of Revenue – Motor Vehicle and Driver Licensing Division",
    "Montana": "Motor Vehicle Division (MVD)",
    "Nebraska": "Department of Motor Vehicles (DMV)",
    "Nevada": "Department of Motor Vehicles (DMV)",
    "New Hampshire": "Division of Motor Vehicles (DMV)",
    "New Jersey": "Motor Vehicle Commission (MVC)",
    "New Mexico": "Motor Vehicle Division (MVD)",
    "New York": "Department of Motor Vehicles (DMV)",
    "North Carolina": "Division of Motor Vehicles (DMV)",
    "North Dakota": "Department of Transportation (DOT)",
    "Ohio": "Bureau of Motor Vehicles (BMV)",
    "Oklahoma": "Department of Public Safety (DPS)",
    "Oregon": "Department of Transportation – Driver and Motor Vehicle Services (DMV)",
    "Pennsylvania": "Department of Transportation – Driver and Vehicle Services (PennDOT)",
    "Rhode Island": "Division of Motor Vehicles (DMV)",
    "South Carolina": "Department of Motor Vehicles (SCDMV)",
    "South Dakota": "Driver Licensing Program – Department of Public Safety",
    "Tennessee": "Department of Safety and Homeland Security",
    "Texas": "Department of Public Safety (DPS)",
    "Utah": "Driver License Division – Department of Public Safety",
    "Vermont": "Department of Motor Vehicles (DMV)",
    "Virginia": "Department of Motor Vehicles (DMV)",
    "Washington": "Department of Licensing (DOL)",
    "West Virginia": "Division of Motor Vehicles (DMV)",
    "Wisconsin": "Division of Motor Vehicles (DMV)",
    "Wyoming": "Department of Transportation – Driver Services Program"
}

descriptions = [
    "Direct Deposit", "ACH Payment", "Check Deposit",
    "POS Purchase", "Debit Card Purchase", "Online Transfer",
    "Loan Repayment"
]

invoice_items = ["Logo Design", "Business Card Design", "Website Mockup", "Social Media Banners", "Brand Guidelines PDF"]

def generate_fake_uk_license():
    name = fake.name()
    first, last = name.split()[0], name.split()[-1]
    dob = fake.date_of_birth().strftime("%d.%m.%Y")
    license_id = f"{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    vehicle = random.choice(vehicle_types)
    address = fake.address().replace("\n", ", ")

    lines = [
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
    return "\n".join(lines)

def generate_fake_us_license():
    state = random.choice(us_states)
    name = fake.name()
    dob = fake.date_of_birth().strftime("%m/%d/%Y")
    license_num = fake.bothify(text="??######")
    address = fake.address().replace("\n", ", ")
    vehicle = random.choice(vehicle_types)
    agency = dmv_agencies[state]

    lines = [
        f"{state.upper()} DRIVER LICENSE",
        f"Name: {name}",
        f"DOB: {dob}",
        f"License #: {license_num}",
        f"Class: {vehicle}",
        f"Issued by: {agency}",
        f"Address: {address}"
    ]
    return "\n".join(lines)


def generate_fake_transaction(date):
    description = random.choice(descriptions)
    amount = round(random.uniform(10.00, 700.00), 2)
    is_credit = description in ["Direct Deposit", "Check Deposit"]

    return {
        "date": date.strftime("%d/%m/%Y"),
        "description": description,
        "debit": "" if is_credit else f"{amount:.2f}",
        "credit": f"{amount:.2f}" if is_credit else ""
    }

def generate_fake_bank_statement(num_transactions=20):
    start_year = random.randint(1900, 2025)
    start_month = random.randint(1, 12)
    start_date = datetime.strptime(f"{start_year}-{start_month}-01", "%Y-%m-%d")
    transactions = []

    for _ in range(num_transactions):
        random_days = random.randint(0, 27)
        trans_date = start_date + timedelta(days=random_days)
        transactions.append(generate_fake_transaction(trans_date))

    name = fake.name()
    account_number = f"XXXX-XXXX-XXXX-{random.randint(1000, 9999)}"

    lines = [
        f"Bank {fake.company()}",
        f"Customer Support: {fake.phone_number()}",
        f"{fake.url()}",
        f"Account Holder: {name}",
        f"Account Number: {account_number}",
        f"Statement Period: {start_year}-{start_month}",
        "",
        "Date       Description              Debit ($)   Credit ($)"
    ]

    for transaction in transactions:
        lines.append(f"{transaction['date']}  {transaction['description']:<24} {transaction['debit']:<11} {transaction['credit']}")

    return "\n".join(lines)

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

    selected_items = random.sample(invoice_items, k=random.randint(2, 4))
    
    lines = [
        f"{sender_company} INVOICE",
        f"Issue Date: {issue_date}",
        f"Due Date: {due_date}",
        f"Invoice #: {invoice_no}",
        f"Billed To: {recipient_name} ({recipient_company})",
        "DESCRIPTION QTY UNIT PRICE TOTAL",
    ]

    subtotal = 0
    for item in selected_items:
        quantity = random.randint(1, 100)
        unit_price = random.randint(1, 1000000)

        total = quantity * unit_price

        subtotal += total
        lines.append(f"{item:<25} {quantity:<5} ${unit_price:<11.2f} ${total:.2f}")
    
    tax = subtotal * 0.05
    total = subtotal + tax

    # Totals
    lines += [
        f"Subtotal: ${subtotal:.2f}",
        f"Tax (5%): ${tax:.2f}",
        f"TOTAL: ${total:.2f}",
        "Payment Info:",
        f"Bank Account: {bank_account}",
        f"Email: {sender_email}",
        f"Phone: {sender_phone}",
        "Please make payment within 30 days."
    ]

    return "\n".join(lines)


def generate_fake_date():
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

    pd.DataFrame(fake_data).to_csv(CSV_PATH, index=False)
