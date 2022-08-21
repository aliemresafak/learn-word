from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Word(BaseModel):
    WordChoices = (
        ("noun", "noun"),
        ("pronoun", "pronoun"),
        ("verb", "verb"),
        ("adjective", "adjective"),
        ("adverb", "adverb"),
        ("preposition", "preposition"),
        ("conjunction", "conjunction"),
        ("interjection", "interjection"),
    )
    name = models.CharField(max_length=100, verbose_name=_("Word"))
    type = models.CharField(max_length=20, choices=WordChoices, null=False)
    meaning = models.TextField(verbose_name=_("Word meaning"), null=False)
    category = models.ForeignKey(
        "category.Category", related_name="words", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name
