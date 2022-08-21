from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
