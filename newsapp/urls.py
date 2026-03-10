from django.urls import path
from . import views 
from .views import home, category_news

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category_news, name='category'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('about/', views.about, name="about"),
]

