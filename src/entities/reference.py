class BookReference:
    def __init__(self, id, title, author, year):
        self.id = id
        self.type = "book"
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"

    def bibtex(self):
        year = str(self.year)
        key = f"{self.author.split()[-1]}{year[2:]}"
        entry = f"""@book{{{key},
    title = {{{self.title}}},
    author = {{{self.author}}},
    year = {{{self.year}}},
}}"""
        return entry

class ArticleReference:
    def __init__(self, id, title, author, year, journal, volume, pages):
        self.id = id
        self.type = "article"
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal
        self.volume = volume
        self.pages = pages

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
    def __init__(self, id, title, author, year, booktitle):
        self.id = id
        self.type = "inproceedings"
        self.title = title
        self.author = author
        self.year = year
        self.booktitle = booktitle

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
