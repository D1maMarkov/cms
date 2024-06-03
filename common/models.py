from django.db import models


class OneInstanceModel(models.Model):
    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        abstract = True


class BlockRelationship(models.Model):
    block_name = models.CharField(verbose_name="Имя компонента", max_length=50, unique=True)
    block = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"

    def __str__(self):
        return self.block_name


class Sortable(models.Model):
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True
        ordering = ["my_order"]


class BasePageBlock(Sortable):
    class Meta(Sortable.Meta):
        abstract = True
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"

    def __str__(self):
        return str(self.name)
