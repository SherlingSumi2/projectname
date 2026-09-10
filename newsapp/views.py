from django.shortcuts import render, get_object_or_404
from datetime import datetime

from .models import (
    SmallSlider,
    News,
    Category,
    Advertisement
)


def home(request):

    # =========================================================
    # SLIDER
    # =========================================================

    sliders = SmallSlider.objects.filter(
        is_active=True
    ).order_by("order")


    # =========================================================
    # ADVERTISEMENTS
    # =========================================================

    banner_ad = Advertisement.objects.filter(
        position="top",
        is_active=True
    ).last()

    right_ad = Advertisement.objects.filter(
        position="right",
        is_active=True
    ).last()

    middle_ad = Advertisement.objects.filter(
        position="middle",
        is_active=True
    ).last()

    bottom_ad = Advertisement.objects.filter(
        position="bottom",
        is_active=True
    ).last()


    # =========================================================
    # BREAKING NEWS
    # =========================================================

    weekend_news = News.objects.filter(
        is_weekend_special=True
    ).order_by("-created_at")


    # =========================================================
    # MAIN FEATURED NEWS
    # =========================================================
    # Admin-la is_featured=True select panna
    # antha news mattum BIG NEWS-a varum.

    main_news_big = News.objects.filter(
        is_featured=True
    ).order_by("-created_at").first()


    # =========================================================
    # OTHER MAIN NEWS
    # =========================================================
    # is_main_news=True irukkura remaining news
    # featured news-ai exclude pannum.

    main_news_list = News.objects.filter(
        is_main_news=True
    ).exclude(
        is_featured=True
    ).order_by("-created_at")


    # =========================================================
    # POPULAR / QUICK UPDATES
    # =========================================================

    popular_news = News.objects.filter(
        is_popular=True
    ).order_by("-created_at")[:5]


    # =========================================================
    # BUSINESS NEWS
    # =========================================================

    business_news = News.objects.filter(
        category__name="Business"
    ).order_by("-created_at")[:6]

    local_news = News.objects.filter(
    is_local_news=True
    ).order_by("-created_at")[:6]


    # =========================================================
    # CONTEXT
    # =========================================================

    context = {
        "categories": Category.objects.all(),

        "sliders": sliders,

        "banner_ad": banner_ad,
        "right_ad": right_ad,
        "middle_ad": middle_ad,
        "bottom_ad": bottom_ad,

        "weekend_news": weekend_news,

        "main_news_big": main_news_big,
        "main_news_list": main_news_list,

        "popular_news": popular_news,

        "business_news": business_news,
        "local_news": local_news,

        "today": datetime.now(),
    }


    return render(
        request,
        "index.html",
        context
    )


# =========================================================
# CATEGORY NEWS
# =========================================================

def category_news(request, slug):

    category = get_object_or_404(
        Category,
        slug=slug
    )

    news_list = News.objects.filter(
        category=category
    ).order_by("-created_at")

    # BOTTOM AD
    bottom_ad = Advertisement.objects.filter(
        position="bottom",
        is_active=True
    ).last()

    return render(
        request,
        "category.html",
        {
            "category": category,
            "news_list": news_list,
            "categories": Category.objects.all(),

            # ADD THIS
            "bottom_ad": bottom_ad,

            "today": datetime.now(),
        }
    )


# =========================================================
# NEWS DETAIL
# =========================================================

def news_detail(request, id):

    news = get_object_or_404(
        News,
        id=id
    )


    related_news = (
        News.objects
        .filter(
            is_weekend_special=False,
            is_popular=False
        )
        .exclude(
            id=id
        )
        .exclude(
            category__slug="business"
        )
        .order_by("-created_at")[:5]
    )


    popular_news = News.objects.filter(
        is_popular=True
    ).exclude(
        id=id
    ).order_by("-created_at")[:5]


    right_ad = Advertisement.objects.filter(
        position="right",
        is_active=True
    ).last()

    bottom_ad = Advertisement.objects.filter(
    position="bottom",
    is_active=True
    ).last()


    return render(
    request,
    "detail.html",
    {
        "news": news,
        "related_news": related_news,
        "popular_news": popular_news,

        "right_ad": right_ad,
        "bottom_ad": bottom_ad,

        "today": datetime.now(),
    }
)


# =========================================================
# ABOUT
# =========================================================

def about(request):

    return render(
        request,
        "about.html",
        {
            "today": datetime.now(),
        }
    )

def tag_news(request, slug):
    tag_name = slug.replace("-", " ")

    news_list = News.objects.filter(
        topic__iexact=tag_name
    ).order_by("-created_at")

    return render(request, "tag.html", {
        "tag_name": tag_name.title(),
        "news_list": news_list,
        "categories": Category.objects.all(),
        "today": datetime.now(),
    })