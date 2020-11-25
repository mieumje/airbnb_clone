from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PostType(AbstractItem):

    """ PostType Model definition """

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    pass


class Photo(core_models.TimeStampedModel):

    """ Photo Model definition """

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="posts_photos")
    blog = models.ForeignKey("Blog", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Blog(core_models.TimeStampedModel):

    """ Blog Model definition """

    CATEGORY_질환 = "질환"
    CATEGORY_예방 = "예방"
    CATEGORY_치료 = "치료"
    CATEGORY_운동 = "운동"

    CATEGORY_CHOICE = (
        (CATEGORY_질환, "질환"),
        (CATEGORY_예방, "예방"),
        (CATEGORY_치료, "치료"),
        (CATEGORY_운동, "운동"),
    )

    name = models.CharField(max_length=140)
    category = models.CharField(
        max_length=5, choices=CATEGORY_CHOICE, blank=True, default=CATEGORY_질환
    )
    description = models.TextField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    post_type = models.ManyToManyField("PostType", related_name="blogs", blank=True)

    def __str__(self):
        return self.name

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url

    def get_next_photos(self):
        photos = self.photos.all()[1:5]
        return photos