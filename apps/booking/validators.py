from django.core.exceptions import ValidationError


def mark_max_value(val):
    if 5 < val < 0:
        raise ValidationError("mark must be between 0 and 5")

