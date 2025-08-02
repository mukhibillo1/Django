from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from ckeditor.fields import RichTextField

from helpers.models import BaseModel


class Add(BaseModel):
    file = models.FileField(_("file"), upload_to="adds/%Y/%m")
    url = models.URLField(_("url"))

    class Meta:
        db_table = "add"
        verbose_name = _("add")
        verbose_name_plural = _("adds")

    @property
    def file_url(self):
        return f"{settings.HOST}{self.file.url}" if self.file else ""

    def __str__(self):
        return f"{self.url}"


class NewsCategory(BaseModel):
    title = models.CharField(_("title"), max_length=256)

    class Meta:
        db_table = "news category"
        verbose_name = _("news category")
        verbose_name_plural = _("news categories")

    def __str__(self):
        return f"{self.title}"


class NewsTag(BaseModel):
    title = models.CharField(_("title"), max_length=256)

    class Meta:
        db_table = "news tag"
        verbose_name = _("news tag")
        verbose_name_plural = _("news tags")

    def __str__(self):
        return f"{self.title}"


class Region(BaseModel):
    title = models.CharField(_("title"), max_length=256)

    class Meta:
        db_table = "region"
        verbose_name = _("region")
        verbose_name_plural = _("regions")

    def __str__(self):
        return f"{self.title}"


class News(BaseModel):
    TYPE_CHOICES = [
        ("supertop", "supertop"),
        ("top", "top"),
        ("editors choice", "editors choice"),
        ("latest", "latest"),
        ("actual", "actual"),
        ("video", "video"),
        ("article", "article"),
        ("interview", "interview"),
        ("announcement", "announcement"),
        ("motivation", "motivation"),
        ("photo", "photo"),
    ]
    title = models.CharField(_("title"), max_length=256)
    category = models.ForeignKey(
        NewsCategory,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="category",
        related_name="news",
    )
    type = models.CharField(_("type"), choices=TYPE_CHOICES,max_length=256)
    tags = models.ManyToManyField(NewsTag, verbose_name="tags", related_name="news", null=True, blank=True)
    region = models.ForeignKey(
        Region,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="region",
        related_name="news",
    )
    cover = models.ImageField(_("cover"), upload_to="news/%Y/%m/%d")
    video = models.URLField(_("video"))
    file = models.FileField(_("file"), upload_to="news/files/%Y/%m/%d", null=True, blank=True)
    time_to_read = models.PositiveIntegerField(_("time to read"), default=0)
    views = models.PositiveIntegerField(_("views"), default=0)
    content = RichTextField(_("content"))
    published_at = models.DateTimeField(_("published_at"), auto_now_add=True) 
    slug = models.SlugField(null=True, blank=True)
    @property
    def cover_url(self):
        return f"{settings.HOST}{self.cover.url}" if self.cover else ""

    @property
    def video_url(self):
        return f"{settings.HOST}{self.video.url}" if self.video else ""

    @property
    def file_url(self):
        return f"{settings.HOST}{self.file.url}" if self.file else ""

    class Meta:
        db_table = "news"
        verbose_name = _("news")
        verbose_name_plural = _("news")

    def __str__(self):
        return f"{self.title}"
