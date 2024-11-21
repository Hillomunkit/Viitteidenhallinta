class Reference:
    def __init__(self, id, title, author, year):
        self.id = id 
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
    
    def bibtex(self):
        key = "TESTI"
        entry = f"""@book{{{key},
    author = {{{self.author}}},
    title = {{{self.title}}},
    year = {{{self.year}}},
}}"""
        return entry