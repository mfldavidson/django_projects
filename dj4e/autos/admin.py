from django.contrib import admin
from autos.models import Make, Auto

class MakeInline(admin.TabularInline):
    model = Make

class AutoInline(admin.TabularInline):
    model = Auto

# Define the admin class
class AutoAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'make', 'mileage', 'comments')
    fields = ['nickname', 'make']

class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AutoInline]

admin.site.register(Make, MakeAdmin)
admin.site.register(Auto, AutoAdmin)
