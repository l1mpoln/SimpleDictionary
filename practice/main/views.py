from django.shortcuts import render, redirect
from . models import Word
from . forms import WordForm


def landing(request):
    return render(request, 'main/base.html')


def adding(request):
    if request.method == 'POST':
        words = WordForm(request.POST)
        words.save()
        return redirect('/home')

    form = WordForm()
    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)


def wordlist(request):
    words = Word.objects.all()
    return render(request, 'main/wordlist.html', {'words': words})
