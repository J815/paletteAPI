from django.db import models

from django.contrib.auth.models import User

class ColorPalette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    dominant_colors = models.CharField(max_length=255)  # Store as comma-separated HEX values
    accent_colors = models.CharField(max_length=255)  # Store as comma-separated HEX values

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    palette = models.ForeignKey(ColorPalette, on_delete=models.CASCADE)
