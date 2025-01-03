from django.db import models

from infrastructure.persistence.models.settings import Font


class FontMixin(models.Model):
    font = models.ForeignKey(Font, verbose_name="Шрифт для текста", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
