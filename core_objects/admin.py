from core_objects.models import *   
from django.contrib import admin
from adminsortable2.admin import *
from core_objects.forms import *

class SlideshowItemInline(SortableInlineAdminMixin, admin.TabularInline):
    model= SlideshowItem
    fields=['headline','bodyText','get_thumbnail_SlideshowItem','image','video','mediaType']
    readonly_fields=['get_thumbnail_SlideshowItem','mediaType']
    form = ResizingForm

    def get_thumbnail_SlideshowItem(self, obj):
        return obj.get_thumbnail_url('x150')
    get_thumbnail_SlideshowItem.short_description = 'thumbnail'

@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
    list_display = (
        'year',
        'get_thumbnail_Slideshow',
        'previewPicture',) 
    inlines=[SlideshowItemInline,]
    

    def get_thumbnail_Slideshow(self, obj):
            return obj.get_thumbnail_url('x100')
    get_thumbnail_Slideshow.short_description = 'thumbnail'