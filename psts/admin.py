from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.PstType)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.psts.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Pst)
class PstAdmin(admin.ModelAdmin):

    """ Pst Admin Definition """

    inlines = (PhotoInline,)

    fields = ["pst_name", "pst_content", "pst_writer", "pst_type", "pst_img"]

    list_display = ("pst_name", "pst_writer", "pst_type", "count_photos")

    raw_id_fields = ("pst_writer",)

    search_fields = ("^pst_name",)

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width= "50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"