from django.contrib import admin
from .models import *

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Order._meta.fields]
    inlines = [ProductInOrderInline]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)
