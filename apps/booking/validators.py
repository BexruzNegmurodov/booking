from django.core.exceptions import ValidationError


def mark_max_value(val):
    if not 6 > val > 0:
        raise ValidationError("mark must be between 0 and 5")

