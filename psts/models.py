from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PstType(AbstractItem):
    """ PstType Model Definition """

    class Meta:
        verbose_name = "Pst Type"
        ordering = ["created"]  # 생성 순으로 정렬


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="pst_photos")
    pst = models.ForeignKey("Pst", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Pst(core_models.TimeStampedModel):

    """ Pst Model Definition """

    pst_name = models.CharField(max_length=20)
    pst_content = models.TextField()
    pst_writer = models.ForeignKey(
        "users.User", related_name="psts", on_delete=models.CASCADE
    )
    pst_type = models.ForeignKey(
        "PstType", related_name="psts", on_delete=models.SET_NULL, null=True
    )
    pst_img = models.ImageField(upload_to="pst_imgs", blank=True)

    def __str__(self):
        return self.pst_name

    def get_absolute_url(self):
        return reverse("psts:list", kwargs={"pk": self.pk})

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url

    def get_next_photos(self):
        photos = self.photos.all()[1:5]
        return photos