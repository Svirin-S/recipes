from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    
}


def hello(request):
    a = 'Hello'
    return HttpResponse(a)


def omlet(request):
    native = [native for native in DATA['omlet'].items()]
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            native[0][0]: native[0][1] * servings,
            native[1][0]: native[1][1] * servings,
            native[2][0]: native[2][1] * servings
        }  
    }
    return render(request, 'index.html', context)


def pasta(request):
    native = [native for native in DATA['pasta'].items()]
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            native[0][0]: native[0][1] * servings,
            native[1][0]: native[1][1] * servings
        }  
    }
    return render(request, 'index.html', context)


def buter(request):
    native = [native for native in DATA['buter'].items()]
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            native[0][0]: native[0][1] * servings,
            native[1][0]: native[1][1] * servings,
            native[2][0]: native[2][1] * servings,
            native[3][0]: native[3][1] * servings
        }  
    }
    return render(request, 'index.html', context)


