import re
from datetime import datetime
class UserInputError(Exception):
    pass

titles = {"book": "Teos",
          "article": "Artikkeli",
          "inproceedings": "Otsikko",
        }

def validate_reference(title, author, year, reference_type, journal=None, volume=None, pages=None, booktitle=None):
    if not title or len(title.strip()) == 0:
        raise UserInputError(f"\"{titles[reference_type]}\" ei voi olla tyhjä")
    if len(title) > 100:
        raise UserInputError(f"\"{titles[reference_type]}\" maksimipituus on 100 merkkiä")
    if not author or len(author.strip()) == 0:
        raise UserInputError("\"Kirjoittanut\" ei voi olla tyhjä")
    if len(author) > 100:
        raise UserInputError("\"Kirjoittanut\" maksimipituus on 100 merkkiä")
    if not re.match(r"^[a-zA-ZåäöÅÄÖ\s'-]+$", author):
        raise UserInputError("\"Kirjoittanut\" sisältää virheellisiä merkkejä")
    current_year = datetime.now().year
    try:
        year_int = int(year)
    except:
        raise UserInputError("\"Painovuosi\" tulee esittää numeroina")
    if year_int < 1000 or year_int > current_year:
        raise UserInputError(f"\"Painovuosi\" tulee olla 1000-{current_year} väliltä")
    if journal:
        if len(journal.strip()) == 0:
          raise UserInputError(f"\"Lehti\" ei voi olla pelkkiä välilyöntejä")
        if len(journal) > 100:
          raise UserInputError(f"\"Lehti\" maksimipituus on 100 merkkiä")
    if volume:
        if len(volume.strip()) == 0:
          raise UserInputError(f"\"Volyymi\" ei voi olla pelkkiä välilyöntejä")
        if len(volume) > 10:
          raise UserInputError(f"\"Volyymi\" tulee olla 1-10 merkkiä")
    if pages:
        if len(pages) > 10:
          raise UserInputError(f"\"Sivut\" tulee olla 1-10 merkkiä")
        if not re.match(r"^\d+(?:[-–]\d+)?$", pages):
            raise UserInputError("\"Sivut\" on virheellisessä formaatissa")
    if booktitle:
        if len(booktitle.strip()) == 0:
            raise UserInputError(f"\"Kirjaotsikko\" ei voi olla pelkkiä välilyöntejä")
        if len(booktitle) > 100:
          raise UserInputError(f"\"Kirjaotsikko\" maksimipituus on 100 merkkiä")
    
    return True