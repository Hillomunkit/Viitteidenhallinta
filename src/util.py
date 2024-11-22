import re
from datetime import datetime
class UserInputError(Exception):
    pass

def validate_reference(title, author, year):
    if not title or len(title.strip()) == 0:
        raise UserInputError("Teos ei voi olla tyhjä")
    if len(title) > 100:
        raise UserInputError("Teoksen nimi ei voi olla enempä kun 100 merkkiä")
    if not author or len(author.strip()) == 0:
        raise UserInputError("Kirjailia ei voi olla tyhjä")
    if len(author) > 100:
        raise UserInputError("Kirjailian nimi ei voi olle enempää kun 100 merkkiä")
    if not re.match(r"^[a-zA-ZåäöÅÄÖ\s'-]+$", author):
        raise UserInputError("Kirjailian nimi sisältää virheellisiä merkkejä")
    current_year = datetime.now().year
    try:
        year_int = int(year)
    except:
        raise UserInputError("Vuosi tulee esittää numeroina")
    if year_int < 1000 or year_int > current_year:
        raise UserInputError(f"Vuosi tulee olla 1000- {current_year} väliltä")
    
    return True