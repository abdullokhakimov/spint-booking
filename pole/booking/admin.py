from django.contrib import admin
from .models import Region, Field, Gallery, Booking
from django.utils.safestring import mark_safe
# Register your models here.

class GalleryInline(admin.TabularInline):
    fk_name = 'field'
    model = Gallery
    extra = 1


class FieldAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'region', 'price', 'get_photo', 'get_photo_counts')
    list_editable = ('price',)
    list_display_links = ('title',)
    list_filter = ('title', 'region', 'price')
    inlines = [GalleryInline]
    prepopulated_fields = {'slug': ('title',)}

    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="65px"')
            except:
                return '-'
        else:
            return '-'

    get_photo.short_description = 'Изображение'

    def get_photo_counts(self, obj):
        if obj.images:
            return str(len(obj.images.all()))
        else:
            return '0'

    get_photo_counts.short_description = 'Количество изображений'

class RegionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'get_fields_count')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title',)

    def get_fields_count(self, obj):
        if obj.fields:
            return str(len(obj.fields.all()))
        else:
            return '0'

    get_fields_count.short_description = 'Количество полей'


admin.site.register(Region, RegionAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Booking)