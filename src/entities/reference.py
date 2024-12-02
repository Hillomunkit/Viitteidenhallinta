class BookReference:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.type = "book"
    # pylint: disable=no-member

    def __str__(self):
        return f"{self.title}, {self.author}, {self.publisher}, {self.year}, {self.volume}, {self.number}, {self.series}, {self.address}, {self.edition}, {self.month}, {self.note}, {self.annote}"

    def bibtex(self):
        year = str(self.year)
        key = f"{self.author.split()[-1]}{year[2:]}"
        entry = f"""@book{{{key},
    title = {{{self.title}}},
    author = {{{self.author}}},
    author = {{{self.publisher}}},
    year = {{{self.year}}},
    volume = {{{self.volume}}},
    number = {{{self.number}}},
    series = {{{self.series}}},
    address = {{{self.address}}},
    edition = {{{self.edition}}},
    month = {{{self.month}}},
    note = {{{self.note}}},
    annote = {{{self.annote}}}
}}"""
        return entry

class ArticleReference:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.type = "article"
    # pylint: disable=no-member

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"

    def bibtex(self):
        year = str(self.year)
        key = f"{self.author.split()[-1]}{year[2:]}"
        entry = f"""@article{{{key},
    title = {{{self.title}}},
    author = {{{self.author}}},
    year = {{{self.year}}},
    journal = {{{self.journal}}},
    volume = {{{self.volume}}},
    pages = {{{self.pages}}},
}}"""
        return entry

class InproceedingsReference:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.type = "inproceedings"
    # pylint: disable=no-member

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"

    def bibtex(self):
        year = str(self.year)
        key = f"{self.author.split()[-1]}{year[2:]}"
        entry = f"""@inproceedings{{{key},
    title = {{{self.title}}},
    author = {{{self.author}}},
    year = {{{self.year}}},
    booktitle = {{{self.booktitle}}},
}}"""
        return entry
