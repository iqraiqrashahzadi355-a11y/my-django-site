from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dish, Contact, Category, Drink, TableBooking
from .forms import ContactForm, BookingForm


# 🏠 Home Page (Top Dishes + Featured Drinks)
def index(request):
    dishes = Dish.objects.all()[:6]  # ✅ Sirf 6 dishes dikhayenge (homepage clean rahe)
    drinks = Drink.objects.all()[:8]  # ✅ Featured 8 drinks
    context = {
        "dishes": dishes,
        "drinks": drinks,
    }
    return render(request, "home/index.html", context)


# ℹ️ About Page
def about(request):
    return render(request, "home/about.html")


# 💼 Services Page
def services(request):
    return render(request, "home/services.html")


# 📬 Contact Page (Form + Success Message)
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Thank you! Your message has been sent successfully.")
            return redirect("contact")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})


# 🍽️ Menu Page (Filter by Category)
def menu(request):
    selected_category = request.GET.get("category")
    categories = Category.objects.all()

    if selected_category:
        dishes = Dish.objects.filter(category__id=selected_category)
    else:
        dishes = Dish.objects.all()

    context = {
        "categories": categories,
        "dishes": dishes,
        "selected_category": int(selected_category) if selected_category else None,
    }
    return render(request, "home/menu.html", context)


# 🥤 Drinks Page (All Drinks)
def drinks(request):
    all_drinks = Drink.objects.all()
    return render(request, "home/drinks.html", {"drinks": all_drinks})


# 🍴 Table Booking Page (Form + Success Message)
def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "✅ Your table has been booked successfully! We look forward to welcoming you soon."
            )
            return redirect("book_table")
        else:
            messages.error(request, "❌ Please check your booking details and try again.")
    else:
        form = BookingForm()

    return render(request, "home/book_table.html", {"form": form})
