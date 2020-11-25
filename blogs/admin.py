from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.PostType)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.blogs.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):

    """ Blog Amin definition """

    inlines = (PhotoInline,)

    list_display = (
        "name",
        "host",
        "count_photos",
    )

    list_filter = ("host",)

    raw_id_fields = ("host",)

    search_fields = ("^name", "^host__username")

    filter_horizontal = ("post_type",)

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"