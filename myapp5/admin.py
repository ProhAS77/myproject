from django.contrib import admin
from .models import Category, Product


@admin.action(description='Сбросить количество до 0')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    # список продуктов
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    # отдельный продукт
    # fields и fieldsets не дружат - либо одно либо другое
    #fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (None, {'classes': ['wide'], 'fields': ['name']}),
        ('Detail', {
            'classes': ['collapse'],
            'description': 'Категория товара и его подробное описание',
            'fields': ['category', 'description']}),
        ('Accounting', {'fields': ['price', 'quantity']}),
        ('Rating and other things', {
            'description': 'Рейтинг на основе оценок покупателей',
            'fields': ['rating', 'date_added']}),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
