class Reference:
    def __init__(self, title, author, year):    # id siirsin tämän sivuun koska reference_repository.py ssä ongelma jos get_referenses käyttää vain 3 argumenttiä.
        #self.id = id #kommentti ylhäällä selittää.
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
