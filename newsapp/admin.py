from django.contrib import admin
from .models import (
    SmallSlider,
    Advertisement,
    BannerAd,
    Category,
    News
)

@admin.register(SmallSlider)
class SmallSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_active')
    list_filter = ('position',)


@admin.register(BannerAd)
class BannerAdAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_at',
        'is_weekend_special',
        'is_main_news',
        'is_popular',
        'likes', 
        'views'
    )
    list_filter = (
        'category',
        'is_weekend_special',
        'is_main_news',
        'is_popular'
    )
    search_fields = ('title',)
