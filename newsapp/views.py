from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import (
    SmallSlider,
    News,
    Category,
    Advertisement,
    BannerAd
)

def home(request):
    # 🔹 SLIDER
    sliders = SmallSlider.objects.filter(
        is_active=True
    ).order_by("order")

    # 🔹 ADS
    banner_ad = BannerAd.objects.filter(
        is_active=True
    ).first()

    right_ad = Advertisement.objects.filter(
        position="right",
        is_active=True
    ).last()

    # 🔹 WEEKEND SPECIAL
    weekend_news = News.objects.filter(
        is_weekend_special=True
    ).order_by('-created_at')

    # 🔥 MAIN NEWS (IMPORTANT PART)
    main_news_qs = News.objects.filter(
        is_main_news=True
    ).order_by('-created_at')

    main_news_big = main_news_qs.first()   # ⭐ One big news
    main_news_list = main_news_qs[1:]      # ⭐ Remaining main news

    # 🔹 POPULAR
    popular_news = News.objects.filter(
        is_popular=True
    ).order_by('-created_at')[:5]

    bottom_ad = Advertisement.objects.filter(
    position="bottom",
    is_active=True
    ).last()

    business_news = News.objects.filter(
        category__slug="business"
    ).order_by("-created_at")[:6]
    
    business_bottom_ad = Advertisement.objects.filter(
    position="business_bottom",
    is_active=True
    ).last()

    context = {
        "categories": Category.objects.all(),
        "sliders": sliders,
        "banner_ad": banner_ad,
        "right_ad": right_ad,
        "weekend_news": weekend_news,
        "main_news_big": main_news_big,
        "main_news_list": main_news_list,
        "popular_news": popular_news,
        "bottom_ad": bottom_ad,
        "business_news": business_news,
        "business_bottom_ad": business_bottom_ad,
        "today": datetime.now(),

    }

    return render(request, "index.html", context)


def category_news(request, slug):
    category = get_object_or_404(Category, slug=slug)

    news_list = News.objects.filter(
        category=category
    ).order_by('-created_at')

    return render(request, "category.html", {
        "category": category,
        "news_list": news_list,
        "categories": Category.objects.all(),
        "today": datetime.now(),
    })


def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    related_news = (
    News.objects
    .filter(is_weekend_special=False, is_popular=False)
    .exclude(id=id)
    .exclude(category__slug="business")
    .order_by('-created_at')[:5]
)

    popular_news = News.objects.filter(
        is_popular=True
    ).exclude(id=id).order_by('-created_at')[:5]

    right_ad = Advertisement.objects.filter(
        position="right",
        is_active=True
    ).last()

    return render(request, "detail.html", {
        "news": news,
        "related_news": related_news,
        "popular_news": popular_news,
        "right_ad": right_ad,
        "today": datetime.now(),
    })

def about(request):
    return render(request, "about.html", {
        "today": datetime.now(),
    })

    



