from msilib.schema import Class
from django.contrib import admin
from blog.models import Note, Categoria

class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "author","publish_date","category", "id"]
    list_editable = ["author", "category"]
    search_fields = ["author","publish_date"]
    list_display_links = ["title"]
    list_per_page = 5

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "id"]
    list_editable = ["description"]
    search_fields = ["name"]
    list_per_page = 5

admin.site.register(Note, NoteAdmin)
admin.site.register(Categoria, CategoriaAdmin)