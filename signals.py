def get_parser(*args, **kwargs):
    from paperless_uyap.parsers import UyapDocumentParser

    return UyapDocumentParser(*args, **kwargs)


def uyap_consumer_declaration(sender, **kwargs):
    return {
        "parser": get_parser,
        "weight": 10,
        "mime_types": {
            "application/zip": ".eyp",
        },
    }
