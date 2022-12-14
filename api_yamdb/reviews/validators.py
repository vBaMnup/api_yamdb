from datetime import datetime

from django.core.exceptions import ValidationError


def check_value_year_valid(value):
    """Проверка что значение года корректно."""
    message = (
        'Невозможно выбрать ненаступивший год для произведения.'
    )
    year_now = datetime.now().year
    if value > year_now:
        raise ValidationError(message)
