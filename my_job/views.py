from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ContactForm()
    context = { 'form': form }
    template_name = 'my_job/home.html'
    return render(request, template_name, context)

# @login_required
# def job_application(request):
#     if request.method == 'POST':
#         form = UserDataForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     form = UserDataForm()
#     context = { 'form': form }
#     template_name = 'my_job/job_application.html'
#     return render(request, template_name, context)
