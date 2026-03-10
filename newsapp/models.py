from django.db import models

class SmallSlider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliders/')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class BannerAd(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="ads/")
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True,null=True)
    video = models.FileField(upload_to='news/videos/', blank=True, null=True)
    is_weekend_special = models.BooleanField(default=False)
    is_main_news = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    POSITION_CHOICES = (
    ('right', 'Right Sidebar'),
    ('top', 'Top Banner'),
    ('middle', 'Middle'),
    ('bottom', 'Bottom Banner'),
    ('business_bottom', 'Business Bottom Banner'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



