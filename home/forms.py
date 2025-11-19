from django import forms
from .models import Contact, TableBooking


# 📬 Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control shadow-sm",
                "placeholder": "Enter your full name",
                "aria-label": "Full Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control shadow-sm",
                "placeholder": "Enter your email address",
                "aria-label": "Email Address"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control shadow-sm",
                "rows": 5,
                "placeholder": "Write your message here...",
                "aria-label": "Message"
            }),
        }


# 🍴 Table Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ["name", "email", "phone", "date", "time", "guests", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control shadow-sm",
                "placeholder": "Your Name",
                "aria-label": "Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control shadow-sm",
                "placeholder": "Your Email",
                "aria-label": "Email"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control shadow-sm",
                "placeholder": "Your Phone Number",
                "aria-label": "Phone Number",
                "pattern": "[0-9]{11}",  # ✅ Optional validation pattern
                "title": "Enter 11-digit phone number"
            }),
            "date": forms.DateInput(attrs={
                "class": "form-control shadow-sm",
                "type": "date",
                "aria-label": "Booking Date"
            }),
            "time": forms.TimeInput(attrs={
                "class": "form-control shadow-sm",
                "type": "time",
                "aria-label": "Booking Time"
            }),
            "guests": forms.NumberInput(attrs={
                "class": "form-control shadow-sm",
                "min": 1,
                "max": 20,
                "aria-label": "Number of Guests"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control shadow-sm",
                "rows": 3,
                "placeholder": "Special requests (optional)",
                "aria-label": "Message"
            }),
        }
