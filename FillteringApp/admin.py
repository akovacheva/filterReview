from django.contrib import admin

# Register your models here.

from FillteringApp.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewerName","reviewFullText","rating","reviewCreatedOnDate")
    list_filter = ("rating","reviewCreatedOnDate")

admin.site.register(Review, ReviewAdmin)

