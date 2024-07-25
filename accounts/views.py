from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('passsword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('project_list')
        else:
            context['has_error'] = True
    return render(request, "login.html", context=context)