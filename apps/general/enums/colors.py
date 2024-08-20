from django.db import models


class ColorChoices(models.TextChoices):
    RED_ORANGE = '#FF5733', 'Red Orange'
    GREEN = '#33FF57', 'Green'
    BLUE = '#3357FF', 'Blue'
    ALICE_BLUE = '#F0F8FF', 'Alice Blue'
    SALMON = '#FA8072', 'Salmon'
    GOLD = '#FFD700', 'Gold'
    CYAN = '#00FFFF', 'Cyan'
    MAGENTA = '#FF00FF', 'Magenta'
    PURPLE = '#800080', 'Purple'
    BLACK = '#000000', 'Black'
    WHITE = '#FFFFFF', 'White'
    GRAY = '#808080', 'Gray'
