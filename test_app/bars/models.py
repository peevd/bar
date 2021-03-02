"""Models"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Bar(models.Model):
    """
    Bar Model
    """

    name = models.TextField(blank=False)
    rating = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
