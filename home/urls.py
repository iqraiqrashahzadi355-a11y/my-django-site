from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="home"),  # 🏠 Home page
    path('about/', views.about, name="about"),  # ℹ️ About page
    path('services/', views.services, name="services"),  # 💼 Services page
    path('contact/', views.contact, name="contact"),  # 📬 Contact page
    path('menu/', views.menu, name="menu"),  # 🍽️ Menu page
    path('drinks/', views.drinks, name="drinks"),  # 🥤 Drinks page
    path('book-table/', views.book_table, name="book_table"),  # 🍴 Table booking page
]

# 🖼️ Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
