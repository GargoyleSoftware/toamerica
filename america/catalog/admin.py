from django.contrib import admin
from models import *

class SocialProfileInline(admin.TabularInline):
    model = SocialProfile

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        SocialProfileInline,
    ]
admin.site.register(Manager, ManagerAdmin)

class RegionalCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
admin.site.register(RegionalCenter, RegionalCenterAdmin)
