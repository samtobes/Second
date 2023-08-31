from django.contrib import admin
from .models import News,Subscribers


class NewsAdmin(admin.ModelAdmin):
    list_display=["title","reporter","date_posted","category"]
    list_editable=["category"]
    list_filter=["category","reporter"]
    prepopulated_fields={"slug":("title",)}

admin.site.register(News,NewsAdmin)
admin.site.register(Subscribers)