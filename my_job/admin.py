from django.contrib import admin
from .models import Contact


# class ContactInline(admin.StackedInline):
#     model = Contact
    


admin.site.register(Contact)
