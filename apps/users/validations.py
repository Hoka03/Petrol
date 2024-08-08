from rest_framework.exceptions import ValidationError


def phone_validate(phone_number: str):
    if not (len(phone_number) == 13
            or
            phone_number.startswith('+998')
            or
            phone_number[1:].isdigit()):
        raise ValidationError('Phone number was mistake, Please try again.')