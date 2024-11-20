class Reference:
    def __init__(self, id, title, author, year):
        self.id = id 
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
