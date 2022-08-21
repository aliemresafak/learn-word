from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Word(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Word"))
    meaning = models.TextField(verbose_name=_("Word meaning"))
    category = models.ForeignKey(
        "category.Category", related_name="words", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name
