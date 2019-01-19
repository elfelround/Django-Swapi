
#admin.site.register(People, PropertyAdmin)
# Register these two together or it will error

from __future__ import unicode_literals

from django.contrib import admin, messages

from .models import (
    People,
    Planet,
    Film,
    Starship,
    Vehicle,
    Species,
    Hero,
    PropertyImage,
)

#class PropertyImageInline(admin.TabularInline):
#    model = PropertyImage
#    extra = 3


#class PropertyAdmin(admin.ModelAdmin):
#    inlines = [PropertyImageInline, ]


classes = [People, Planet, Film, Starship, Vehicle, Species, Hero, PropertyImage]


class ModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            messages.error(request, "Only superusers can change models")
            return False
        return super(ModelAdmin, self).save_model(request, obj, form, change)

for c in classes:
    admin.site.register(c, ModelAdmin)
