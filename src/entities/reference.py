import re

# pylint: disable=no-member
class ReferenceBase:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.fields = {}

    def __str__(self):
        return ", ".join(str(value) for value in self.fields.values() if value != "")

    def __generate_citekey(self):
        author_parts = re.split(r'[,\s]+', self.author)
        key_author = author_parts[0].lower()
        key_year = str(self.year)
        words = re.split(r'\W+', self.title)
        ignore = {"a", "an", "the", ""}
        filtered_words = [word.lower() for word in words if word.lower() not in ignore]
        key_title = filtered_words[0] if len(filtered_words) > 0 else ""

        return f"{key_author}{key_year}{key_title}"

    def bibtex(self):
        citekey = self.__generate_citekey()

        bibtex_fields = "\n".join(
            f"  {field_key} = {{{field_value}}},"
            for field_key, field_value in self.fields.items() if field_value != ""
        )

        entry = (
            f"@{self.type}{{{citekey},\n"
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
