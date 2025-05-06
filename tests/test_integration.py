import os
import pytest
from src.classifier import classify_file
from werkzeug.datastructures import FileStorage

BANK_STATEMENT_DIR = "files/bank_statement/"
INVOICE_DIR = "files/invoice/"
DRIVERS_LICENCE = "files/drivers_licence/"

def get_test_file(file_path: str):
    file = open(file_path, "rb")
    return FileStorage(stream=file, filename=os.path.basename(file_path)), file

def get_file_paths(directory):
    return [ os.path.join(directory, file) for file in os.listdir(directory) ]

bank_statement_files = get_file_paths(BANK_STATEMENT_DIR)
invoice_files = get_file_paths(INVOICE_DIR)
drivers_licence_files = get_file_paths(DRIVERS_LICENCE)

@pytest.mark.parametrize("file_path", bank_statement_files)
def test_bank_statement_files(file_path):
    file_storage, file_stream = get_test_file(file_path)
    try:
        predicted = classify_file(file_storage)
        assert predicted == "bank_statement"
    finally:
        file_stream.close()

@pytest.mark.parametrize("file_path", invoice_files)
def test_invoice_files(file_path):
    file_storage, file_stream = get_test_file(file_path)
    try:
        predicted = classify_file(file_storage)
        assert predicted == "invoice"
    finally:
        file_stream.close()

@pytest.mark.parametrize("file_path", drivers_licence_files)
def test_drivers_licence_files(file_path):
    file_storage, file_stream = get_test_file(file_path)
    try:
        predicted = classify_file(file_storage)
        assert predicted == "drivers_licence"
    finally:
        file_stream.close()
