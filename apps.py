from django.apps import AppConfig

from paperless_uyap.signals import uyap_consumer_declaration


class PaperlessUyapConfig(AppConfig):
    name = "paperless_uyap"

    def ready(self):
        from documents.signals import document_consumer_declaration

        document_consumer_declaration.connect(uyap_consumer_declaration)

        AppConfig.ready(self)
