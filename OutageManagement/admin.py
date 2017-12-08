from django.contrib import admin

# Register your models here.

from .models import Outage, Outage_Service

# Minimal registration of Outage.
admin.site.register(Outage)
admin.site.register(Outage_Service)


# class OutageInline(admin.TabularInline):
#     """
#     Defines format of inline book insertion (used in AuthorAdmin)
#     """
#     model = Outage
#
#
# @admin.register(OutageService)
# class OutageAdmin(admin.ModelAdmin):
#     """
#     Administration object for Outage models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - adds inline addition of OutageManagement instances in OutageManagement view (inlines)
#     """
#
# admin.site.register(Outage,OutageAdmin)

