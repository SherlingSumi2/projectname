from .models import Category


def navbar_categories(request):

    fixed_categories = [
        "kerala",
        "national",
        "world",
        "politics",
        "business",
        "sports",
        "cinema",
    ]

    categories = Category.objects.exclude(
        slug__in=fixed_categories
    ).order_by("name")

    return {
        "navbar_categories": categories
    }