import re
from datetime import datetime
class UserInputError(Exception):
    pass

def validate_reference(title, author, year):
    if not title or len(title.strip()) == 0:
        raise UserInputError("Title can't be empty")
    if len(title) > 100:
        raise UserInputError("Maximum title length is 100 characters")
    if not author or len(author.strip()) == 0:
        raise UserInputError("Author can't be empty")
    if len(author) > 100:
        raise UserInputError("Maximum author length is 100 characters")
    if not re.match(r"^[a-zA-ZåäöÅÄÖ\s'-]+$", author):
        raise UserInputError("Author name contains invalid characters")
    current_year = datetime.now().year
    try:
        year_int = int(year)
    except:
        raise UserInputError("Year must be a valid integer")
    if year_int < 1000 or year_int > current_year:
        raise UserInputError(f"Year must be between 1000 and {current_year}")
    
    return True