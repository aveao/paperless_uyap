from pathlib import Path
from zipfile import ZipFile

from documents.parsers import ParseError
from paperless_tesseract.parsers import RasterisedDocumentParser


class UyapDocumentParser(RasterisedDocumentParser):
    """
    This parser extracts the UstYazi/ustyazi.pdf from the .eyp file and passes it to the PDF parser.
    """

    _inner_pdf_path = None

    def _get_inner_pdf_path(self, document_path: Path) -> Path:
        # If the pdf is already extracted, return that instead
        if self._inner_pdf_path:
            return self._inner_pdf_path

        # Open the zip
        try:
            eyp_zip = ZipFile(document_path)
        except Exception as e:
            raise ParseError(f"Failed to open zipfile {document_path}") from e

        # Check if the inner PDF is there
        extraction_path = self.tempdir / "inner_pdf.pdf"
        inner_pdf_path = "UstYazi/ustyazi.pdf"
        if inner_pdf_path not in eyp_zip.namelist():
            raise ParseError(
                f"{inner_pdf_path} not found in {document_path}, cannot proceed.",
            )

        # Extract inner PDF and save it in the temp dir
        with (
            eyp_zip.open(inner_pdf_path, "r") as compressed_pdf,
            Path.open(extraction_path, "wb") as extraction_file,
        ):
            extraction_file.write(compressed_pdf.read())

        # Save the PDF path and return it
        self._inner_pdf_path = extraction_path
        return extraction_path

    def get_thumbnail(self, document_path: Path, mime_type, file_name=None) -> Path:
        return super().get_thumbnail(
            document_path=self._get_inner_pdf_path(document_path),
            mime_type="application/pdf",
            file_name=file_name,
        )

    def parse(self, document_path, mime_type, file_name=None):
        return super().parse(
            document_path=self._get_inner_pdf_path(document_path),
            mime_type="application/pdf",
            file_name=file_name,
        )

    def get_page_count(self, document_path, mime_type):
        return super().get_page_count(
            document_path=self._get_inner_pdf_path(document_path),
            mime_type="application/pdf",
        )

    def extract_metadata(self, document_path, mime_type):
        return super().extract_metadata(
            document_path=self._get_inner_pdf_path(document_path),
            mime_type="application/pdf",
        )
