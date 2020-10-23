from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [fields.name for fields in Subscriber._meta.fields]
    list_filter = ["name",]
    search_fields = ["email", "name"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
