class BookReference:
    def __init__(self, id, title, author, year):
        self.id = id 
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
    
    def bibtex(self):
        key = "testi"
        entry = f"""@book{{{key},
    title = {{{self.title}}},
    author = {{{self.author}}},
    year = {{{self.year}}},
}}"""
        return entry