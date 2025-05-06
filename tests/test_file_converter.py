import io
from src.file_converter import extract_text
from werkzeug.datastructures import FileStorage

fake_pdf = FileStorage(
    stream=io.BytesIO(b"%PDF-1.4\n% Fake content"),
    filename="fake.pdf",
    content_type="application/pdf"
)

fake_png = FileStorage(
    stream=io.BytesIO(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"),
    filename="fake.png",
    content_type="image/png"
)

fake_jpg = FileStorage(
    stream=io.BytesIO(b"\xff\xd8\xff\xe0\x00\x10JFIF"),
    filename="fake.jpg",
    content_type="image/jpeg"
)

fake_csv = FileStorage(
    stream=io.StringIO("name,email\nAlice,alice@example.com\nBob,bob@example.com"),
    filename="fake.csv",
    content_type="text/csv"
)

def test_pdf(mocker):
    mocker.patch("src.file_converter.extract_text_from_pdf", return_value="Test Data")

    text = extract_text(fake_pdf)
    assert text == "Test Data"

def test_png(mocker):
    mocker.patch("src.file_converter.extract_text_from_image", return_value="Test Data")

    text = extract_text(fake_png)
    assert text == "Test Data"

def test_jpg(mocker):
    mocker.patch("src.file_converter.extract_text_from_image", return_value="Test Data")

    text = extract_text(fake_jpg)
    assert text == "Test Data"

def test_unsupported_file():
    text = extract_text(fake_csv)
    assert text is None

