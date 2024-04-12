from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skill = prof.skill_set.exclude(description__exact="")
    other_skill = prof.skill_set.filter(description="")

    context = {
        'profile': prof,
        'top_skill': top_skill,
        'other_skill': other_skill
               }
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            print('Пользователь не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Имя или пароль неверны')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    return redirect('login')




