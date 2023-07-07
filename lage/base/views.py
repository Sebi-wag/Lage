from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date



@login_required
def home(request):
    user = request.user

    today = date.today()
    if user.datum:
        lage = (user.datum.date() - today).days
    else:
        lage = "--"

    context = {"user": user, "lage": lage}
    return render(request, 'base/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if email == "sebastian19.wagner@gmail.com":
                return redirect("https://www.spreadshirt.at/shop/design/du+kek+unisex+hoodie-D5b182dc4c8056369db208080?sellable=dYb1OVdnx7ikYlbX02yE-1047-23")
            else:
                try:
                    user = User.objects.get(email=email)
                    login(request, user)
                except User.DoesNotExist:
                    user = User.objects.create_user(email=email, username=email)
                    login(request, user)
                return redirect(reverse('home'))
    else:
        form = SignUpForm()
    
    return render(request, 'base/signup.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('signup')


@csrf_exempt
def update_datum(request):
    if request.method == 'POST':
        datum = request.POST.get('datum', None)
        if datum:
            request.user.datum = datum
            request.user.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})