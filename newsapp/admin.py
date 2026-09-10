from django.contrib import admin
from django import forms

from .models import (
    SmallSlider,
    Advertisement,
    Category,
    News
)


class NewsAdminForm(forms.ModelForm):

    topic = forms.ChoiceField(
        required=False,
        choices=(),
        label="Topic"
    )

    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        topics = (
            SmallSlider.objects
            .filter(is_active=True)
            .values_list("title", flat=True)
            .distinct()
            .order_by("title")
        )

        self.fields["topic"].choices = [
            ("", "--------- Select Topic ---------")
        ] + [
            (topic, topic)
            for topic in topics
        ]

# =========================================================
# TRENDING NEWS
# =========================================================

@admin.register(SmallSlider)
class SmallSliderAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'order',
        'is_active',
    )

    list_editable = (
        'order',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
    )

    ordering = (
        'order',
        '-created_at',
    )


# =========================================================
# ADVERTISEMENTS
# =========================================================

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):

    list_display = (
        'position',
        'image',
        'is_active',
    )

    list_filter = (
        'position',
        'is_active',
    )

    list_editable = (
        'is_active',
    )

    ordering = (
        'position',
    )


# =========================================================
# CATEGORY
# =========================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
    )

    search_fields = (
        'name',
    )

    exclude = (
        'slug',
    )


# =========================================================
# NEWS
# =========================================================

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
   

    list_display = (
        'title',
        'category',
        'created_at',

        'is_featured',
        'is_main_news',
        'is_weekend_special',
        'is_popular',
        'is_local_news',

        'likes',
        'views',
    )


    # =====================================================
    # FILTER
    # =====================================================

    list_filter = (
        'category',

        'is_featured',
        'is_main_news',
        'is_weekend_special',
        'is_popular',
        'is_local_news',

        'created_at',
    )


    # =====================================================
    # SEARCH
    # =====================================================

    search_fields = (
    'title',
    'content',
    'topic',
)


    # =====================================================
    # EDIT DIRECTLY FROM NEWS LIST
    # =====================================================

    list_editable = (
        'is_featured',
        'is_main_news',
        'is_weekend_special',
        'is_popular',
        'is_local_news',
    )


    # =====================================================
    # ORDER
    # =====================================================

    ordering = (
        '-created_at',
    )


    # =====================================================
    # FORM FIELD ORDER
    # =====================================================

    fields = (
    'category',
    'title',
    'content',
    'image',
    'video',

    'topic',
    'link',

    'is_featured',
    'is_main_news',
    'is_weekend_special',
    'is_popular',
    'is_local_news',

    'likes',
    'views',
)


    # =====================================================
    # READ ONLY
    # =====================================================

    readonly_fields = (
        'created_at',
    )