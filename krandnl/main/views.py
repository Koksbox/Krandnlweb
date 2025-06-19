from django.shortcuts import render

def home(request):
    context = {
        'title': 'Главная страница',
        'description': 'Добро пожаловать на сайт, посвящённый игре Крестики-нолики!'
    }
    return render(request, 'main/home.html', context)

def about_app(request):
    blocks = range(1, 8)
    return render(request, 'main/about_app.html', {'blocks': blocks})

def tictactoe(request):
    return render(request, 'main/tictactoe.html') 