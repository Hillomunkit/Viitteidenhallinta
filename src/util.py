class UserInputError(Exception):
    pass

#Tänne toteutetaan syötteiden tarkistus, käytä näitä app.py ja validate_reference_test.py
def validate_reference(content):
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
          raise UserInputError("Todo content length must be smaller than 100")
