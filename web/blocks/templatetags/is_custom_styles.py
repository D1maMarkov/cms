from django import template

from infrastructure.persistence.models.styles.styles.base_custom_styles import (
    BaseCustomStyles,
)

register = template.Library()


@register.simple_tag()
def is_custom_styles(block) -> bool:
    return isinstance(block, BaseCustomStyles)
