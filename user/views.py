from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserDataForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserRegisterForm()
    template_name = 'user/register.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def job_application(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            userdata = form.save(commit=False)
            userdata.user = request.user
            userdata.save()
            return redirect('home')
    form = UserDataForm()
    context = { 'form': form }
    template_name = 'user/job_application.html'
    return render(request, template_name, context)