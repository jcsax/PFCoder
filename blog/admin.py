from msilib.schema import Class
from django.contrib import admin
from blog.models import Economy, Entertainment, Health
# Register your models here.

class EntretainmentAdmin(admin.ModelAdmin):
    list_display = ["title", "author","publish_date"]
    list_editable = ["author",]
    search_fields = ["author","publish_date"]
    list_per_page = 5
admin.site.register(Entertainment, EntretainmentAdmin)

class EconomyAdmin(admin.ModelAdmin):
    list_display= ["title", "author","publish_date"]
    list_editable = [ "author",]
    search_fields = ["author","publish_date"]
    list_per_page = 5
admin.site.register(Economy, EconomyAdmin)

class HealthAmin(admin.ModelAdmin):
    list_display= ["title", "author","publish_date"]
    list_editable = ["author",]
    search_fields = ["author","publish_date"]
    list_per_page = 5
admin.site.register(Health, HealthAmin)
