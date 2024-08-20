from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm

from .models import Station, StationPetrolMark


class StationPetrolMarkLine(admin.StackedInline):
    model = StationPetrolMark


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}
    inlines = (StationPetrolMarkLine,)