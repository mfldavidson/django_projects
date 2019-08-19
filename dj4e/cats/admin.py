from django.contrib import admin
from cats.models import Breed, Cat

class BreedInline(admin.TabularInline):
    model = Breed

class CatInline(admin.TabularInline):
    model = Cat

# Define the admin class
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CatInline]

class CatAdmin(admin.ModelAdmin):
    list_display = ('nickname','breed','weight','foods')

admin.site.register(Breed, BreedAdmin)
admin.site.register(Cat, CatAdmin)
