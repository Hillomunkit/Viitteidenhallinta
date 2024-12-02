# pylint: disable=no-member
class ReferenceBase:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.fields = {}

    def __str__(self):
        return ", ".join(str(value) for value in self.fields.values() if value != "")

    def bibtex(self):
        year = str(self.year)
        key = f"{self.author.split()[-1]}{year[2:]}"

        bibtex_fields = "\n".join(
            f"  {field_key} = {{{field_value}}},"
            for field_key, field_value in self.fields.items() if field_value != ""
        )

        entry = (
            f"@{self.type}{{{key},\n"
            f"{bibtex_fields}\n"
            f"}}"
        )
        return entry


class BookReference(ReferenceBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "book"
        self.fields = {
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "year": self.year,
            "volume": self.volume,
            "number": self.number,
            "series": self.series,
            "address": self.address,
            "edition": self.edition,
            "month": self.month,
            "note": self.note,
            "annote": self.annote,
        }


class ArticleReference(ReferenceBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "article"
        self.fields = {
            "title": self.title,
            "author": self.author,
            "journal": self.journal,
            "year": self.year,
            "volume": self.volume,
            "number": self.number,
            "pages": self.pages,
            "month": self.month,
            "note": self.note,
            "annote": self.annote,
        }


class InproceedingsReference(ReferenceBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "inproceedings"
        self.fields = {
            "title": self.title,
            "author": self.author,
            "booktitle": self.booktitle,
            "year": self.year,
            "editor": self.editor,
            "volume": self.volume,
            "number": self.number,
            "series": self.series,
            "pages": self.pages,
            "month": self.month,
            "address": self.address,
            "organization": self.organization,
            "publisher": self.publisher,
            "note": self.note,
            "annote": self.annote,
        }
