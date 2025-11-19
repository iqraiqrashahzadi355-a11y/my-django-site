from django.contrib import admin
from .models import Dish, Category, Drink, Contact, TableBooking, ClientReview

# 🧾 Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# 🍽️ Dish Admin
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

# 🍹 Drink Admin
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

# 📬 Contact Messages Admin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'message')

# 🍴 Table Booking Admin
@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'guests', 'created_at')
    list_filter = ('date', 'guests')
    search_fields = ('name', 'email', 'phone')

# 💬 Client Reviews Admin
admin.site.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('name', 'comment')
