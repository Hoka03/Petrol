from rest_framework.exceptions import ValidationError


def phone_validate(phone_number: str):
    if not (len(phone_number) == 13
            and
            phone_number.startswith('+998')
            and
            phone_number[1:].isdigit()):
        raise ValidationError('Phone number was mistake, Please try again.')