from domain.materials.document import DocumentInterface, DocumentPatternInterface
from domain.materials.repository import DocumentRepositoryInterface
from infrastructure.persistence.models.materials import Document, DocumentFormatPattern


class DocumentRepository(DocumentRepositoryInterface):
    def get_document(self, document_slug: str) -> DocumentInterface:
        try:
            return Document.objects.get(slug=document_slug)
        except Document.DoesNotExist:
            return None

    def get_document_patterns(self, document_slug: str) -> list[DocumentPatternInterface]:
        return DocumentFormatPattern.objects.filter(document__slug=document_slug)

    def get_documents(self) -> list[DocumentInterface]:
        return Document.objects.values("title", "slug").all()


def get_document_repository() -> DocumentRepositoryInterface:
    return DocumentRepository()