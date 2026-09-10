from django.db import models
from django.utils.text import slugify
from urllib.parse import urlparse, parse_qs


class SmallSlider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliders/')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Trending News"
        verbose_name_plural = "Trending News"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='news/videos/',
        blank=True,
        null=True
    )

    topic = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    # =====================================================
    # NEWS OPTIONS
    # =====================================================

    is_weekend_special = models.BooleanField(
        default=False,
        verbose_name="Breaking News"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Top News"
    )

    is_main_news = models.BooleanField(
        default=False,
        verbose_name="Main News"
    )

    is_popular = models.BooleanField(
        default=False,
        verbose_name="Quick Updates"
    )

    is_local_news = models.BooleanField(
    default=False,
    verbose_name="Local News"
    )

    # =====================================================
    # OPTIONAL NEWS LINK
    # =====================================================

    link = models.URLField(
    blank=True,
    null=True,
    verbose_name="YouTube Link"
    )

    # =====================================================
    # META
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.PositiveIntegerField(
        default=0
    )

    views = models.PositiveIntegerField(
        default=0
    )

@property
def youtube_id(self):
    if not self.link:
        return None

    url = self.link.strip()
    parsed = urlparse(url)

    # youtube.com/watch?v=VIDEO_ID
    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed.query).get("v", [None])[0]

    # youtu.be/VIDEO_ID
    if parsed.hostname == "youtu.be":
        return parsed.path.strip("/").split("/")[0]

    # youtube.com/shorts/VIDEO_ID
    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        parts = parsed.path.strip("/").split("/")
        if len(parts) >= 2 and parts[0] == "shorts":
            return parts[1]

    return None
    
    def __str__(self):
        return self.title


class Advertisement(models.Model):

    POSITION_CHOICES = (
        ('top', 'Top Banner'),
        ('right', 'Right Banner'),
        ('middle', 'Middle Banner'),
        ('bottom', 'Bottom Banner'),
    )

    image = models.ImageField(upload_to='ads/')
    link = models.URLField(blank=True, null=True)

    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_position_display()
