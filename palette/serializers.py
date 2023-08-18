# serializers.py

from rest_framework import serializers
from .models import ColorPalette

class ColorPaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorPalette
        fields = '__all__'
