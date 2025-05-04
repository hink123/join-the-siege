ALLOWED_EXTENSIONS = {"pdf", "png", "png", "jpg", "jpeg"}
IMAGE_TYPES = {"png", "jpg", "jpeg"}

INDUSTRIES = ["bank_statement", "drivers_licence", "invoice"]
INDUSTRIES_ENCODED = {industry: i for i, industry in enumerate(INDUSTRIES)}
INDUSTRIES_DECODED = {i: industry for industry, i in INDUSTRIES_ENCODED.items()}

MODEL_LOCATION = "classifier_model/"
GENERATED_DATA_LOCATION = "files/processed_data/generated_text_with_labels.csv"

US_STATES = [
    "Alaska", 
    "Alabama", 
    "Arkansas", 
    "Arizona", 
    "California", 
    "Colorado", 
    "Connecticut", 
    "Delaware", 
    "Florida", 
    "Georgia", 
    "Hawaii", 
    "Iowa", 
    "Idaho", 
    "Illinois", 
    "Indiana", 
    "Kansas", 
    "Kentucky", 
    "Louisiana", 
    "Massachusetts", 
    "Maryland", 
    "Maine", 
    "Michigan", 
    "Minnesota", 
    "Missouri", 
    "Mississippi", 
    "Montana", 
    "North Carolina", 
    "North Dakota", 
    "Nebraska", 
    "New Hampshire", 
    "New Jersey", 
    "New Mexico", 
    "Nevada", 
    "New York", 
    "Ohio", 
    "Oklahoma", 
    "Oregon", 
    "Pennsylvania", 
    "Rhode Island", 
    "South Carolina", 
    "South Dakota", 
    "Tennessee", 
    "Texas", 
    "Utah", 
    "Virginia", 
    "Vermont", 
    "Washington", 
    "Wisconsin", 
    "West Virginia", 
    "Wyoming"
]

VEHICLE_TYPES = ["Motorcycle", "Car", "Commercial Vehicle", "3 Wheeler Only"]

US_DMV_AGENCIES = {
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

TRANSACTION_EXAMPLES = [
    "Direct Deposit", 
    "ACH Payment", 
    "Check Deposit",
    "POS Purchase", 
    "Debit Card Purchase", 
    "Online Transfer",
    "Loan Repayment"
]

CREDIT_TRANSACTIONS = ["Direct Deposit", "Check Deposit"]

INVOICE_EXAMPLES = [
    "Logo Design",
    "Business Card Design", 
    "Website Mockup", 
    "Social Media Banners", 
    "Brand Guidelines PDF"
]
